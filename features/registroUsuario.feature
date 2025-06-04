Feature: Registro de Usuario en Automation Exercise

  Scenario: Registro exitoso de un nuevo usuario
    Given El usuario navega al sitio principal
    When Abre el formulario de registro
    And Ingresa los datos requeridos y crea la cuenta
    Then El nombre del usuario debe mostrarse en la página principal
