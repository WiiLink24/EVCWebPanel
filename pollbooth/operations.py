from flask import render_template, flash

from pollbooth.forms import DeleteForm


def manage_delete_item(item_id: int, type_name: str, callback) -> str:
    form = DeleteForm()
    if form.validate_on_submit():
        # This is quite easily circumvented.
        # However, all we need is for the user to pay attention.
        if form.given_id.data == item_id:
            return callback()
        else:
            flash(f"Incorrect {type_name}!")
    return render_template(
        "delete_item.html", form=form, item_id=item_id, type_name=type_name
    )
