import pandas as pd
from http import HTTPStatus
from .serializers import search_text_schema
from docsumo.utils import get_csv_file_path_for_name
from docsumo.utils import Rectangle, is_rectangle_in_inside_inner_rectangle
from flask import Blueprint, jsonify, request
from marshmallow.exceptions import ValidationError

blueprint = Blueprint('api', __name__)


@blueprint.route('/search/text/', methods=('POST',))
def search_text():
    data = request.get_json()

    # validate user input
    try:
        validated_data = search_text_schema.load(data)
    except ValidationError as e:
        return jsonify(e.normalized_messages()), HTTPStatus.BAD_REQUEST

    file_name = validated_data["file_name"]
    position = validated_data["position"]

    # Load csv file in pandas
    file_path = get_csv_file_path_for_name(file_name)
    df = pd.read_csv(file_path)

    # create a new column- `rect_coordinates` which has instance of `Rectangle` dataclass
    df["rect_coordinates"] = df.apply(
        lambda x: Rectangle(
            x1=x["x0"],
            y1=x["y0"],
            x2=x["x2"],
            y2=x["y0"]
        ), axis=1
    )

    # Create `Rectangle` instance of outer rectangle
    outer_rect = Rectangle(
        x1=position[0], y1=position[1], x2=position[2], y2=position[3]
    )
    df["is_inside_outer_rect"] = df["rect_coordinates"].apply(
        lambda x: is_rectangle_in_inside_inner_rectangle(
            outer_rect, x
        )
    )

    # Filter rows by `is_inside_outer_rect` = True
    inside_rect_df = df.loc[df['is_inside_outer_rect'] == True]
    texts = inside_rect_df['Text'].to_list()
    text = ' '.join([str(text) for text in texts])
    return jsonify({"text": text}), HTTPStatus.OK
