from flask import redirect, render_template, request, url_for
from werkzeug import exceptions

from models import Suggestions, db
from app import app
from pollbooth.operations import manage_delete_item
from pollbooth.admin import oidc
from pollbooth.utils.countries import languages, countries  # Import the data from countries.py

@app.route("/thepollbooth/suggestions")
def list_suggestions():
    page_num = request.args.get("page", default=1, type=int)

    suggestions = Suggestions.query.order_by(Suggestions.id.asc()).paginate(
        page=page_num, per_page=100, error_out=False
    )
    
    # Process suggestions to add human-readable country, region, and language names
    processed_suggestions = []
    for suggestion in suggestions.items:
        country_name = "Unknown"
        if str(suggestion.country_code) in countries:
            country_data = countries[str(suggestion.country_code)]
            country_name = country_data.get("Name", "Unknown")
        
        region_name = "Unknown"
        if str(suggestion.country_code) in countries:
            country_data = countries[str(suggestion.country_code)]
            if "Subregions" in country_data and str(suggestion.region_code) in country_data["Subregions"]:
                region_data = country_data["Subregions"][str(suggestion.region_code)]
                region_name = region_data.get("en", "Unknown")  # Using English name
        
        language_name = "Unknown"
        if 0 <= suggestion.language_code < len(languages):
            language_name = languages[suggestion.language_code]
        
        suggestion.country_name = country_name
        suggestion.region_name = region_name
        suggestion.language_name = language_name
        processed_suggestions.append(suggestion)
    
    suggestions.items = processed_suggestions

    return render_template(
        "suggestion_list.html",
        suggestions=suggestions,
        type_length=suggestions.total,
        type_max_count=100,
        main=True
    )

@app.route("/thepollbooth/suggestions/<int:suggestion_id>/remove", methods=["GET", "POST"])
@oidc.require_login
def remove_suggestion(suggestion_id: int):
    def drop_suggestion():
        db.session.delete(current_suggestion)
        db.session.commit()

        return redirect(url_for("list_suggestions"))

    current_suggestion = Suggestions.query.filter(
        Suggestions.id == suggestion_id
    ).first()

    if not current_suggestion:
        return exceptions.NotFound()

    return manage_delete_item(suggestion_id, "suggestion", drop_suggestion)