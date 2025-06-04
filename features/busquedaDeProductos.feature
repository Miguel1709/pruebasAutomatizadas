Feature: Búsqueda de Productos en Automation Exercise

  Scenario: Búsqueda de productos por palabra clave "dress"
    Given El usuario navega al sitio principal
    When Accede a la sección de productos
    And Ingresa "dress" en el campo de búsqueda
    And Presiona el botón de búsqueda
    Then Se muestran resultados relacionados con "dress"