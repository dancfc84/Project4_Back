

from models.book_listing import BookListingModel
from models.books import BookModel
from models.authors import AuthorModel
from models.book_condition import BookConditionModel
from models.book_type import BookTypeModel
from models.genres import GenreModel
from models.users import UserModel
from models.comments import CommentModel
from models.book_listing import BookListingModel


listing_data = [
    BookListingModel(type_id=1, condition_id=1, user_id=1)
]

users_list = [
  UserModel(first_name="Daniel", last_name="Whittock", username="dwhittock", address1="Halstead, Orchard Grove", address2="Chalfont St Peter", county="bucks", postcode="SL9 9EX", password="Dan1231984", email="dan@gmail.com", credits=5, rating=0)
]

authors_list = [
    AuthorModel(first_name="Brett Easton", last_name="Ellis")
]

book_condition_list = [
    BookConditionModel(condition="Like New"),
    BookConditionModel(condition="Excellent"),
    BookConditionModel(condition="Good"),
    BookConditionModel(condition="satisfactory"),
    BookConditionModel(condition="Poor")
]

type_list = [
    BookTypeModel(type="Paperback"),
    BookTypeModel(type="Hardback")
]

genre_list = [
    GenreModel(genre="Thriller"),
    GenreModel(genre="Adventure"),
    GenreModel(genre="Romance"),
    GenreModel(genre="Contemporary"),
    GenreModel(genre="Dystopian"),
    GenreModel(genre="Mystery"),
    GenreModel(genre="Horror"),
    GenreModel(genre="Science Fiction"),
    GenreModel(genre="Children"),
    GenreModel(genre="Memoir"),
    GenreModel(genre="Autobiography"),
    GenreModel(genre="Biography"),
    GenreModel(genre="Cookbook"),
    GenreModel(genre="Art"),
    GenreModel(genre="Self-help"),
    GenreModel(genre="Health"),
    GenreModel(genre="History"),
    GenreModel(genre="Travel"),
    GenreModel(genre="Humour")
]

books_list  = [
    BookModel( name="American Psycho", year_released=1991, rating=4.2, listing=listing_data ,description="Set in Manhattan during the Wall Street boom of the late 1980s, American Psycho follows the life of wealthy young investment banker Patrick Bateman. Bateman, in his mid-20s when the story begins, narrates his everyday activities, from his recreational life among the Wall Street elite of New York to his forays into murder by night. Through present tense stream-of-consciousness narrative, Bateman describes his daily life, ranging from a series of Friday nights spent at nightclubs with his colleagues—where they snort cocaine, critique fellow club-goers' clothing, trade fashion advice, and question one another on proper etiquette—to his loveless engagement to fellow yuppie Evelyn and his contentious relationship with his brother and senile mother.", image="https://welcometothewriterslife.com/wp-content/uploads/2018/07/American-Psycho.jpg", pages=399, user_id=1, genre_id=1, author_id=1 ),
]

book_listing_list = [
    BookListingModel(type_id=1, condition_id=1, user_id=1)
]

comment_list = [
    CommentModel(content="Great book", book_id=1, user_id=1)
]


