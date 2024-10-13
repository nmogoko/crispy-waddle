from models import ReadingList, ContentCalendar
from flask_marshmallow import Marshmallow

marshmallow = Marshmallow()

class ReadingListSchema(marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        models = ReadingList


class ContentCalendarSchema(marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        models  = ContentCalendar
