from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config
from schemas import ReadingListSchema, ContentCalendarSchema
from models import ReadingList, ContentCalendar

app = Flask(__name__)
app.config.from_object(Config)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dpg-cs0kerggph6c73aa9nig-a.oregon-postgres.render.com:5432/group_four'
# static route
reading_list_schema = ReadingListSchema(many=True)
reading_list_schema_single = ReadingListSchema()
content_calendar_schema = ContentCalendarSchema(many=True)

db = SQLAlchemy(app)

@app.route('/reading-list')
def get_reading_lists():
    reading_lists = ReadingList.query.all()
    return reading_list_schema.jsonify(reading_lists)

@app.route('/wallets')
def get_wallets():
    return 'All the wallets returned'

# dynamic route


@app.route('/wallets/<int:id>')
def get_wallet(id):
    return 'Hi, this is coming from wallet {}'.format(str(id))


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
