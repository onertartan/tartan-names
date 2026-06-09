from __future__ import annotations

import argparse
import asyncio
from pathlib import Path

from playwright.async_api import async_playwright


STREAMLIT_PRINT_CSS = """
header,
footer,
#MainMenu,
.stAppHeader,
.stDeployButton,
[data-testid="stSidebar"],
[data-testid="stSidebarNav"],
[data-testid="collapsedControl"] {
    display: none !important;
    visibility: hidden !important;
}

[data-testid="stAppViewContainer"],
[data-testid="stMain"],
.main,
.block-container {
    margin: 0 !important;
    padding: 12px !important;
    max-width: 100% !important;
    width: 100% !important;
}

* {
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
}
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Export the rendered Streamlit main panel to a clean PDF."
    )
    parser.add_argument("--url", default="http://localhost:8501", help="Streamlit app URL.")
    parser.add_argument(
        "--output",
        default="temp/exports/streamlit_panel.pdf",
        help="PDF file path to write.",
    )
    parser.add_argument("--viewport-width", type=int, default=1920)
    parser.add_argument("--viewport-height", type=int, default=1080)
    parser.add_argument(
        "--wait-ms",
        type=int,
        default=5000,
        help="Extra wait after Streamlit loads, for charts/widgets to settle.",
    )
    parser.add_argument(
        "--scale",
        type=float,
        default=0.57,
        help="PDF scale. Lower values fit wider/taller panels onto one page.",
    )
    parser.add_argument(
        "--format",
        default="A4",
        help="PDF page format, for example A4, A3, Letter.",
    )

 #   parser.add_argument("--portrait", action="store_true",help="Use portrait orientation. Default is landscape.")
    parser.add_argument(
        "--browser-channel",
        default="msedge",
        help="Installed browser channel to use. Use chromium if Playwright Chromium is installed.",
    )
    parser.add_argument(
        "--headed",
        action="store_true",
        help="Open a visible controlled browser window before exporting.",
    )
    parser.add_argument(
        "--pause-before-export",
        action="store_true",
        help="Wait for Enter before export, useful for manually setting Streamlit controls.",
    )
    return parser.parse_args()


async def export_streamlit_to_pdf(args: argparse.Namespace) -> None:
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)

    async with async_playwright() as playwright:
        launch_kwargs = {"headless": not args.headed}
        if args.browser_channel:
            launch_kwargs["channel"] = args.browser_channel

        try:
            browser = await playwright.chromium.launch(**launch_kwargs)
        except Exception:
            launch_kwargs.pop("channel", None)
            browser = await playwright.chromium.launch(**launch_kwargs)

        page = await browser.new_page(
            viewport={"width": args.viewport_width, "height": args.viewport_height},
            device_scale_factor=1,
        )

        await page.goto(args.url, wait_until="networkidle")
        await page.wait_for_selector("[data-testid='stAppViewContainer']", timeout=30000)
        await page.wait_for_timeout(args.wait_ms)
        await page.emulate_media(media="screen")
        await page.add_style_tag(content=STREAMLIT_PRINT_CSS)

        if args.pause_before_export:
            await asyncio.to_thread(
                input,
                "Adjust the Streamlit panel in the opened browser, then press Enter to export PDF...",
            )
            await page.add_style_tag(content=STREAMLIT_PRINT_CSS)

        await page.pdf(
            path=str(output),
            format=args.format,
            landscape=True,
           # landscape=not args.portrait,
            print_background=True,
            scale=args.scale,
            margin={
                "top": "8mm",
                "right": "8mm",
                "bottom": "8mm",
                "left": "8mm",
            },
        )

        await browser.close()
        print(f"PDF saved to: {output.resolve()}")


def main() -> None:
    asyncio.run(export_streamlit_to_pdf(parse_args()))


if __name__ == "__main__":
    main()
