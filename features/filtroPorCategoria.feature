Feature: Filtrado de Productos por Categoría en Automation Exercise

  Scenario: Filtrar productos por categoría "Women" y subcategoría "Tops"
    Given El usuario navega al sitio principal
    When Regresa a la sección de productos
    And Selecciona la categoría "Women"
    And Selecciona la subcategoría "Tops"
    Then Se muestran productos de la categoría Tops
