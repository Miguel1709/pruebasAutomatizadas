Feature: Añadir Productos al Carrito en Automation Exercise

  Scenario: Añadir el primer producto de búsqueda al carrito
    Given El usuario navega al sitio principal
    When Accede a la sección de productos
    And Ingresa "dress" en el campo de búsqueda
    And Presiona el botón de búsqueda
    Then Se muestran resultados relacionados con "dress"
    And Agrega el primer producto de búsqueda al carrito

  Scenario: Añadir el primer producto filtrado por categoría al carrito
    Given El usuario navega al sitio principal
    When Regresa a la sección de productos
    And Selecciona la categoría "Women"
    And Selecciona la subcategoría "Tops"
    Then Se muestran productos de la categoría Tops
    And Agrega el primer producto al carrito
