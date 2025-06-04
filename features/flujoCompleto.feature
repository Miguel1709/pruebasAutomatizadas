Feature: Flujo completo en Automation Exercise

  Scenario: Registro, navegación, búsqueda, filtro y carrito
    Given El usuario navega al sitio principal
    When Abre el formulario de registro
    And Ingresa los datos requeridos y crea la cuenta
    Then El nombre del usuario debe mostrarse en la página principal

    When Accede a la sección de productos
    And Ingresa "dress" en el campo de búsqueda
    And Presiona el botón de búsqueda
    Then Se muestran resultados relacionados con "dress"
    And Agrega el primer producto de búsqueda al carrito

    When Regresa a la sección de productos
    And Selecciona la categoría "Women"
    And Selecciona la subcategoría "Tops"
    Then Se muestran productos de la categoría Tops
    And Agrega el primer producto al carrito

    When El usuario accede al carrito de compras
    And Presiona el botón "Proceed To Checkout"
    Then Es redirigido a la página de checkout

    When Hace scroll hasta el botón "Place Order"
    And Presiona el botón "Place Order"
    Then Es redirigido a la página de pago

    When Ingresa los datos de la tarjeta y confirma el pago
    Then El pedido se realiza correctamente

    When Descarga la factura de la compra
    And Presiona el botón "Continue"
    Then Es redirigido al inicio
