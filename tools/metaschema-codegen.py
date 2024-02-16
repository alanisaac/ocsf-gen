"""
Generates the internal Pydantic models for OCSF schema definition files from the various metaschemas.

NOTE: running this script is a bit manual. datamodel-code-generator does not handle non-pythonic characters 
      in file names well, even though they are valid for json-schema.  In order to run this script, you need
      to tweak the metaschema file names and #ref references to eliminate the `.schema` extension and to use
      underscores (_) in places of hyphens (-).  It should not need to be run often though.
"""
import sys
from pathlib import Path
from datamodel_code_generator import InputFileType, generate
from datamodel_code_generator import DataModelType, PythonVersion


def main():
    args = sys.argv[1:]
    input_directory = Path(args[0])
    output_directory = Path(__file__).parent.parent / "src" / "ocsf_gen" / "models"

    generate(
        input_directory,
        input_file_type=InputFileType.JsonSchema,
        output=output_directory,
        output_model_type=DataModelType.PydanticV2BaseModel,
        target_python_version=PythonVersion.PY_310,
        snake_case_field=True,
        use_schema_description=True,
    )

if __name__ == "__main__":
    main()