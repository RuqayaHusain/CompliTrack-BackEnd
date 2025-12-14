from models.tea import TeaModel
from models.comment import CommentModel

# List of teas to seed into the database
teas_list = [
    TeaModel(name="chai", rating=4, in_stock=True),
    TeaModel(name="earl grey", rating=3, in_stock=False),
    TeaModel(name="matcha", rating=3, in_stock=True),
    TeaModel(name="green tea", rating=5, in_stock=True),
    TeaModel(name="black tea", rating=4, in_stock=True),
    TeaModel(name="oolong", rating=4, in_stock=False),
    TeaModel(name="hibiscus", rating=4, in_stock=True),
    TeaModel(name="peppermint", rating=5, in_stock=True),
    TeaModel(name="jasmine", rating=3, in_stock=True)
]

# List of comments related to teas
# Each comment is associated with a tea using the tea_id
comments_list = [
    CommentModel(content="This is a great tea", tea_id=1),
    CommentModel(content="Perfect for relaxing evenings", tea_id=2),
    CommentModel(content="I love the vibrant green color!", tea_id=3),
    CommentModel(content="So refreshing and healthy!", tea_id=4),
    CommentModel(content="A classic choice for any time of day", tea_id=5)
]
