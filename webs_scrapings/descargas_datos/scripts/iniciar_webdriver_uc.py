import undetected_chromedriver as uc


def iniciar_webdriver(headless=False, pos="maximizada"):
    """Inicia un navegador de Chrome y devuelve el objeto Webdriver instanciado.
    pos: indica la posicion del navegador en la pantalla ("maximizada" | "izquierda" | "derecha")"""

    # instanciamos las opciones de Chrome
    options = uc.ChromeOptions()
    # desactivamos las notificaciones
    options.add_argument("--disable-notifications")
    # desactivamos la traducción de páginas
    options.add_argument("--disable-features=Translate")
    # desactivamos el guardado de credenciales
    options.add_argument("--password-store=basic")
    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enable": False
        }
    )
    # iniciamos el driver
    driver = uc.Chrome(
        options=options,
        # version_main=chrome_version,
        headless=headless,
        log_level=3
    )
    if not headless:
        driver.maximize_window()
        # driver.set_window_size(1400, 1400)
        # driver.set_window_position(0, 0)
        if pos != "maximizada":
            # Obtenemos la resolucion de la ventana
            ancho, alto = driver.get_window_size().values()
            if pos == "izquierda":
                # posicionamos la ventana en la mitad izquierda de la pantalla
                driver.set_window_rect(x=0, y=0, width=ancho//2, height=alto)
            elif pos == "derecha":
                driver.set_window_rect(
                    x=ancho//2, y=0, width=ancho//2, height=alto)
    return driver
