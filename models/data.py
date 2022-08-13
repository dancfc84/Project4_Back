

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
    AuthorModel(first_name="--Choose an", last_name="option--"),
    AuthorModel(first_name="Brett Easton", last_name="Ellis"),
    AuthorModel(first_name="Ian", last_name="McEwan"),
    AuthorModel(first_name="Irvine", last_name="Welsh"),
    AuthorModel(first_name="George", last_name="Orwell"),
    AuthorModel(first_name="George", last_name="Saunders"),
    AuthorModel(first_name="Elizabeth", last_name="Von Arnim"),
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
    GenreModel(genre="--Choose an option--"),
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
    GenreModel(genre="Humour"),
    GenreModel(genre="Short Story"),
]

books_list  = [
    BookModel( name="American Psycho", year_released=1991, rating=4.2, listing=listing_data ,description="Set in Manhattan during the Wall Street boom of the late 1980s, American Psycho follows the life of wealthy young investment banker Patrick Bateman. Bateman, in his mid-20s when the story begins, narrates his everyday activities, from his recreational life among the Wall Street elite of New York to his forays into murder by night. Through present tense stream-of-consciousness narrative, Bateman describes his daily life, ranging from a series of Friday nights spent at nightclubs with his colleagues—where they snort cocaine, critique fellow club-goers' clothing, trade fashion advice, and question one another on proper etiquette—to his loveless engagement to fellow yuppie Evelyn and his contentious relationship with his brother and senile mother.", image="https://welcometothewriterslife.com/wp-content/uploads/2018/07/American-Psycho.jpg", pages=399, user_id=1, genre_id=5, author_id=2 ),
    BookModel( name="Trainspotting", year_released=1993, rating=4.2, listing=listing_data ,description="Trainspotting is the first novel by Scottish writer Irvine Welsh, first published in 1993. It takes the form of a collection of short stories, written in either Scots, Scottish English or British English, revolving around various residents of Leith, Edinburgh who either use heroin, are friends of the core group of heroin users, or engage in destructive activities that are effectively addictions", image="https://newgstudio.com/wp-content/uploads/2016/05/trainspotting1.jpg", pages=344, user_id=1, genre_id=5, author_id=4 ),
    BookModel( name="Nineteen Eighty-Four", year_released=1949, rating=4.2, listing=listing_data ,description="The book is set in 1984 in Oceania, one of three perpetually warring totalitarian states (the other two are Eurasia and Eastasia). Oceania is governed by the all-controlling Party, which has brainwashed the population into unthinking obedience to its leader, Big Brother.", image="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1532714506l/40961427._SX318_.jpg", pages=328, user_id=1, genre_id=2, author_id=5 ),
    BookModel( name="Tenth of December", year_released=2013, rating=4.2, listing=listing_data ,description="Tenth of December is a collection of short stories by American author George Saunders. It includes stories published in various magazines between 1995 and 2012", image="https://images-eu.bookshop.org/images/9781408894811.jpg?height=500&v=v4-66c23e91867b9410805481299e9171b3", pages=208, user_id=1, genre_id=5, author_id=6 ),
    BookModel( name="Vera", year_released=1993, rating=4.2, listing=listing_data ,description="Lucy Entwhistle and Everard Wemyss are both reeling from recent unhappiness when they meet and swiftly fall in love. Lucy is Wemyss's 'sweet girl', and to Lucy, Everard is the whole world. The only blot on Lucy's happiness is the shadowy figure of Wemyss's first wife, Vera, who died in mysterious circumstances. But it is not until the happy couple return home and begin their life of wedded bliss that Lucy really begins to wonder: what did happen to Vera?", image="https://images-eu.bookshop.org/images/9781784872335.jpg?height=500&v=v4-a1da3d42a01c17c089618f3e29d093fd", pages=344, user_id=1, genre_id=5, author_id=7 ),
]

book_listing_list = [
    BookListingModel(type_id=1, condition_id=1, user_id=1)
]

comment_list = [
    CommentModel(content="Great book", book_id=1, user_id=1)
]


