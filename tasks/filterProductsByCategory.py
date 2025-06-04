import allure
from actors.actor import Actor
from interactions.clickOn import ClickOn
from interactions.scrollTo import ScrollTo
from ui.productListeningElements import ProductListingElements

class FilterProductsByCategory:
    """
    Una Tarea que permite a un Actor filtrar productos por categoría y subcategoría.
    """
    def __init__(self, category: str, subcategory: str):
        self.category = category
        self.subcategory = subcategory
        self.description = f"filtrar productos por categoría '{category}' y subcategoría '{subcategory}'"

    @classmethod
    def by_women_and_tops(cls):
        """
        Método de fábrica para filtrar por categoría "Women" y subcategoría "Tops".
        """
        return cls(category="Women", subcategory="Tops")

    def perform_as(self, actor: Actor):
        """
        El Actor realiza la tarea de filtrar productos.
        """
        actor.attempts_to(
            ScrollTo.the_element(ProductListingElements.WOMEN_CATEGORY_LINK),
            ClickOn.the(ProductListingElements.WOMEN_CATEGORY_LINK),
            ScrollTo.the_element(ProductListingElements.TOPS_SUBCATEGORY_LINK),
            ClickOn.the(ProductListingElements.TOPS_SUBCATEGORY_LINK)
        )
