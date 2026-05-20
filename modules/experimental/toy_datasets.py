# Set up cluster parameters
import pickle
import time
import warnings
from pathlib import Path
from itertools import cycle, islice
import numpy as np

from sklearn import cluster, datasets
from matplotlib import pyplot as plt
from matplotlib.lines import Line2D
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score
from sklearn_extra.cluster import KMedoids

from clustering.models.ga_clusterer import GAEngine, dunn_index

N_GA_RUNS = 30
CROSSOVER_RATES = [0.7, 0.8, 0.9]
MUTATION_RATES = [0.001, 0.002, 0.005, 0.01, 0.02]
SELECTION_METHODS = ["rank", "roulette", "tournament"]

n_samples = 50
noisy_circles = datasets.make_circles(n_samples=n_samples, factor=0.5, noise=0.0, random_state=170)
noisy_moons = datasets.make_moons(n_samples=n_samples, noise=0.0, random_state=170)
blobs = datasets.make_blobs(n_samples=n_samples, random_state=170)
rng = np.random.RandomState(170)
no_structure = rng.rand(n_samples, 2), None

# Anisotropicly distributed data
X, y = datasets.make_blobs(n_samples=n_samples, random_state=170,centers=3)
transformation = [[0.6, -0.6], [-0.4, 0.8]]
X_aniso = np.dot(X, transformation)
aniso = (X_aniso, y)

# blobs with varied variances
varied = datasets.make_blobs(n_samples=n_samples, cluster_std=[1.0, 2.5, 0.5], random_state=170)
# Set up cluster parameters
plt.figure(figsize=(9 * 1.3 + 2, 14.5))
plt.subplots_adjust(left=0.02, right=0.98, bottom=0.001, top=0.96, wspace=0.05, hspace=0.01)

plot_num = 1

default_base = {"n_neighbors": 10, "n_clusters": 3}

datasets = [
    (noisy_circles, {"n_clusters": 2}),
    (noisy_moons, {"n_clusters": 2}),
    (varied, {"n_neighbors": 2}),
    (aniso, {"n_neighbors": 2}),
    (blobs, {"centers":3}),
   # (no_structure, {}),
]


def _safe_metric_value(metric_fn, X, labels):
    unique_labels = np.unique(labels)
    if len(unique_labels) < 2 or len(unique_labels) >= len(labels):
        return "n/a"

    try:
        return f"{metric_fn(X, labels):.3f}"
    except Exception:
        return "n/a"


def _metric_value(metric_fn, X, labels):
    unique_labels = np.unique(labels)
    if len(unique_labels) < 2 or len(unique_labels) >= len(labels):
        return np.nan

    try:
        return float(metric_fn(X, labels))
    except Exception:
        return np.nan


def _format_mean_std(values):
    values = np.asarray(values, dtype=float)
    values = values[~np.isnan(values)]
    if values.size == 0:
        return "n/a"
    return f"{values.mean():.3f} +/- {values.std():.3f}"


def _run_ga_multiple_times(ga_engine, X, n_runs=N_GA_RUNS):
    metric_names = (
        ("silhouette", silhouette_score),
        ("davies_bouldin", davies_bouldin_score),
        ("calinski_harabasz", calinski_harabasz_score),
        ("dunn", dunn_index),
    )
    aggregated_metrics = {name: [] for name, _ in metric_names}
    fitness_histories = []
    best_run = None

    for run_idx in range(n_runs):
        current_engine = GAEngine(
            data=X,
            n_clusters=ga_engine.n_clusters,
            num_generations=ga_engine.num_generations,
            sol_per_pop=ga_engine.sol_per_pop,
            elitism_count=ga_engine.elitism_count,
            crossover_rate=ga_engine.crossover_rate,
            mutation_rate=ga_engine.mutation_rate,
            saturate_after=ga_engine.saturate_after,
            selection_method=ga_engine._selector.method,
            tournament_size=ga_engine._selector.tournament_size,
            truncation_ratio=ga_engine._selector.truncation_ratio,
            metric_fun=ga_engine.metric_fun,
            maximize=ga_engine.maximize,
            random_state=run_idx,
        )
        current_engine.fit(X)
        labels = current_engine.labels_.astype(int)

        for metric_name, metric_fn in metric_names:
            aggregated_metrics[metric_name].append(_metric_value(metric_fn, X, labels))

        fitness_histories.append(np.asarray(current_engine.fitness_history_, dtype=float))

        if best_run is None or current_engine.best_fitness_ > best_run.best_fitness_:
            best_run = current_engine

    max_history_len = max(len(history) for history in fitness_histories)
    padded_histories = np.full((n_runs, max_history_len), np.nan)
    for idx, history in enumerate(fitness_histories):
        padded_histories[idx, : len(history)] = history
        if len(history) < max_history_len:
            padded_histories[idx, len(history):] = history[-1]

    return {
        "best_engine": best_run,
        "metric_values": aggregated_metrics,
        "mean_fitness_history": np.nanmean(padded_histories, axis=0),
        "std_fitness_history": np.nanstd(padded_histories, axis=0),
    }


def _plot_ga_fitness_summary(dataset_name, algorithm_name, mean_history, std_history, config=None):
    plt.figure(figsize=(8, 4))
    generations = np.arange(1, len(mean_history) + 1)
    plt.plot(generations, mean_history, linewidth=2, label="Mean best fitness")
    plt.fill_between(
        generations,
        mean_history - std_history,
        mean_history + std_history,
        alpha=0.2,
        label="+/-1 std",
    )
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    if config is None:
        title_suffix = f"{N_GA_RUNS} runs"
    else:
        title_suffix = (
            f"{N_GA_RUNS} runs | {config['selection_method']} | "
            f"cx={config['crossover_rate']} | mut={config['mutation_rate']}"
        )
    plt.title(f"{dataset_name} - {algorithm_name} ({title_suffix})")
    plt.legend()
    plt.tight_layout()


def _save_ga_summary_pickle(ga_run_summary, dataset_name, algorithm_name, output_dir="results/ga_summaries"):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    config = ga_run_summary["config"]
    file_name = (
        f"{dataset_name.replace(' ', '_')}"
        f"__{algorithm_name.replace(' ', '_')}"
        f"__selection_{config['selection_method']}"
        f"__crossover_{config['crossover_rate']}"
        f"__mutation_{config['mutation_rate']}.pkl"
    )
    file_path = output_path / file_name

    with file_path.open("wb") as handle:
        pickle.dump(ga_run_summary, handle)

    return file_path


def _grid_search_ga_configs(ga_engine, X, dataset_name, algorithm_name):
    metric_name_map = {
        silhouette_score: "silhouette",
        davies_bouldin_score: "davies_bouldin",
        calinski_harabasz_score: "calinski_harabasz",
        dunn_index: "dunn",
    }
    objective_metric_name = metric_name_map.get(ga_engine.metric_fun)
    best_summary = None

    for selection_method in SELECTION_METHODS:
        for crossover_rate in CROSSOVER_RATES:
            for mutation_rate in MUTATION_RATES:
                current_engine = GAEngine(
                    data=X,
                    n_clusters=ga_engine.n_clusters,
                    num_generations=ga_engine.num_generations,
                    sol_per_pop=ga_engine.sol_per_pop,
                    elitism_count=ga_engine.elitism_count,
                    crossover_rate=crossover_rate,
                    mutation_rate=mutation_rate,
                    saturate_after=ga_engine.saturate_after,
                    selection_method=selection_method,
                    tournament_size=ga_engine._selector.tournament_size,
                    truncation_ratio=ga_engine._selector.truncation_ratio,
                    metric_fun=ga_engine.metric_fun,
                    maximize=ga_engine.maximize,
                )
                ga_run_summary = _run_ga_multiple_times(current_engine, X, N_GA_RUNS)
                ga_run_summary["config"] = {
                    "selection_method": selection_method,
                    "crossover_rate": crossover_rate,
                    "mutation_rate": mutation_rate,
                    "metric_name": objective_metric_name or getattr(ga_engine.metric_fun, "__name__", "unknown"),
                    "maximize": ga_engine.maximize,
                    "dataset_name": dataset_name,
                    "algorithm_name": algorithm_name,
                    "n_runs": N_GA_RUNS,
                }
                if objective_metric_name is not None:
                    objective_values = ga_run_summary["metric_values"][objective_metric_name]
                else:
                    objective_values = [
                        _metric_value(ga_engine.metric_fun, X, ga_run_summary["best_engine"].labels_.astype(int))
                    ]

                objective_values = np.asarray(objective_values, dtype=float)
                objective_values = objective_values[~np.isnan(objective_values)]
                ga_run_summary["objective_mean"] = (
                    float(objective_values.mean()) if objective_values.size else np.nan
                )

                _save_ga_summary_pickle(ga_run_summary, dataset_name, algorithm_name)

                if best_summary is None:
                    best_summary = ga_run_summary
                    continue

                if ga_engine.maximize:
                    if ga_run_summary["objective_mean"] > best_summary["objective_mean"]:
                        best_summary = ga_run_summary
                else:
                    if ga_run_summary["objective_mean"] < best_summary["objective_mean"]:
                        best_summary = ga_run_summary

    return best_summary


for i_dataset, (dataset, algo_params) in enumerate(datasets):
    # update parameters with dataset-specific values
    params = default_base.copy()
    params.update(algo_params)

    X, y = dataset

    # normalize dataset for easier parameter selection
    X = StandardScaler().fit_transform(X)

    # ============
    # Create cluster objects
    #0.001, 0.005, 0.01, 0.05, 0.1

    ga_silhouette = GAEngine(X, n_clusters=params["n_clusters"] ,metric_fun= silhouette_score)
    ga_davies_bouldin = GAEngine(X, n_clusters=params["n_clusters"] ,metric_fun= davies_bouldin_score,maximize=False)
    ga_calinski_harabasz= GAEngine(X, n_clusters=params["n_clusters"] ,metric_fun= calinski_harabasz_score)
    ga_dunn = GAEngine(X, n_clusters=params["n_clusters"], metric_fun=dunn_index, selection_method="rank",mutation_rate=0.002)
    k_means = KMeans(n_clusters=params["n_clusters"])
    k_medoids = KMedoids(n_clusters=params["n_clusters"])
    clustering_algorithms = (
      #  ("Silhouette Score", ga_silhouette),
       # ("Davies-Bouldin", ga_davies_bouldin),
        #("Calinski-Harabasz", ga_calinski_harabasz),
       # ("Dunn Index", ga_dunn),
        ("K-Means",k_means),("K-Medoids",k_medoids)
    )

    dataset_name = f"Dataset {i_dataset + 1}"

    for name, algorithm in clustering_algorithms:
        t0 = time.time()

        # catch warnings related to kneighbors_graph
        with warnings.catch_warnings():
            warnings.filterwarnings(
                "ignore",
                message="the number of connected components of the "
                "connectivity matrix is [0-9]{1,2}"
                " > 1. Completing it to avoid stopping the tree early.",
                category=UserWarning,
            )
            if isinstance(algorithm, GAEngine):
                ga_run_summary = _grid_search_ga_configs(algorithm, X, dataset_name, name)
                algorithm = ga_run_summary["best_engine"]
            else:
                ga_run_summary = None
                algorithm.fit(X)

        t1 = time.time()
        if hasattr(algorithm, "labels_"):
            y_pred = algorithm.labels_.astype(int)
        else:
            y_pred = algorithm.predict(X)

        ax = plt.subplot(len(datasets), len(clustering_algorithms), plot_num)
        if i_dataset == 0:
            ax.set_title(name, size=18)

        colors = np.array(
            list(
                islice(
                    cycle(
                        [
                            "#377eb8",
                            "#ff7f00",
                            "#4daf4a",
                            "#f781bf",
                            "#a65628",
                            "#984ea3",
                            "#999999",
                            "#e41a1c",
                            "#dede00",
                        ]
                    ),
                    int(max(y_pred) + 1),
                )
            )
        )
        ax.scatter(X[:, 0], X[:, 1], s=10, color=colors[y_pred])

        if ga_run_summary is None:
            silhouette_value = _safe_metric_value(silhouette_score, X, y_pred)
            davies_bouldin_value = _safe_metric_value(davies_bouldin_score, X, y_pred)
            calinski_harabasz_value = _safe_metric_value(calinski_harabasz_score, X, y_pred)
            dunn_value = _safe_metric_value(dunn_index, X, y_pred)
        else:
            silhouette_value = _format_mean_std(ga_run_summary["metric_values"]["silhouette"])
            davies_bouldin_value = _format_mean_std(ga_run_summary["metric_values"]["davies_bouldin"])
            calinski_harabasz_value = _format_mean_std(ga_run_summary["metric_values"]["calinski_harabasz"])
            dunn_value = _format_mean_std(ga_run_summary["metric_values"]["dunn"])
            _plot_ga_fitness_summary(
                dataset_name=dataset_name,
                algorithm_name=name,
                mean_history=ga_run_summary["mean_fitness_history"],
                std_history=ga_run_summary["std_fitness_history"],
                config=ga_run_summary["config"],
            )

        metric_handles = [
            Line2D([], [], linestyle="none", label=f"Silhouette: {silhouette_value}"),
            Line2D([], [], linestyle="none", label=f"Davies-Bouldin: {davies_bouldin_value}"),
            Line2D([], [], linestyle="none", label=f"Calinski-Harabasz: {calinski_harabasz_value}"),
            Line2D([], [], linestyle="none", label=f"Dunn: {dunn_value}"),
        ]
        ax.legend(
            handles=metric_handles,
            loc="upper left",
            framealpha=0.9,
            handlelength=0,
            handletextpad=0,
            borderpad=0.4,
            fontsize=9,
        )

        ax.set_xlim(-2.5, 2.5)
        ax.set_ylim(-2.5, 2.5)
        ax.set_xticks(())
        ax.set_yticks(())
        ax.text(
            0.99,
            0.01,
            ("%.2fs" % (t1 - t0)).lstrip("0"),
            transform=ax.transAxes,
            size=15,
            horizontalalignment="right",
        )
        plot_num += 1
    #    if  isinstance(algorithm,GAEngine):
     #       algorithm.plot_fitness()

plt.show()
"""
import numpy as np
MAX_N = 50
l = np.zeros((MAX_N,))
l[0]=1
l[1]=2
l[2]=4
l[3]=8
l[4]=16
for i in range(4,MAX_N):
    l[i]=2*l[i-1]-l[i-5]#2*l[i-1]-l[i-2]+2*l[i-3]-l[i-4]
    if i==5:
        print(l[5])
S=0
for i in range(MAX_N):
    S+= l[i]/(2**(i+5))
print(S)
"""
