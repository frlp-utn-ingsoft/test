import re
from playwright.sync_api import Page, expect


def test_youtube_search_and_play(page: Page):
    # 1. Ir a YouTube
    page.goto("https://www.youtube.com", timeout=60000)

    # 3. Completar campo de búsqueda y enviar
    search_input = page.get_by_role("combobox", name="Buscar")
    search_input.fill("Playwright tutorial")
    search_input.press("Enter")

    # 4. Esperar que aparezcan resultados y hacer clic en el primero
    page.wait_for_selector("ytd-video-renderer", timeout=10000)
    first_result = page.locator("ytd-video-renderer").first
    first_result.click()

    # 5. Verificar que el título y el reproductor estén visibles
    expect(page.get_by_role("heading", level=1)).to_be_visible()
    expect(page.locator("video").first).to_be_visible()
