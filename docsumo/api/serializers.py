import os
from marshmallow import (
    Schema,
    fields,
    ValidationError,
    validates_schema,
)

from docsumo.utils import get_csv_file_path_for_name


class SearchTextSchema(Schema):
    file_name = fields.Str(required=True)
    position = fields.List(
        fields.Int(required=True), required=True
    )

    @validates_schema
    def validate_position(self, data, **kwargs):
        if len(data['position']) != 4:
            raise ValidationError("`position` field requires 4 values- x0, y0, x2, y2")
        file_name = data["file_name"]
        file_path = get_csv_file_path_for_name(file_name)
        if not os.path.isfile(file_path):
            raise ValidationError("Invalid file name- %s" % file_name)


search_text_schema = SearchTextSchema()
