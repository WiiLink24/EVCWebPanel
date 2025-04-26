from flask import redirect, render_template, request, url_for
from werkzeug import exceptions

from models import Questions, db
from pollbooth.forms import QuestionForm
from app import app
from pollbooth.operations import manage_delete_item
from pollbooth.admin import oidc


@app.route("/thepollbooth/questions")
@oidc.require_login
def list_questions():
    page_num = request.args.get("page", default=1, type=int)

    questions = Questions.query.order_by(Questions.question_id.asc()).paginate(
        page=page_num, per_page=100, error_out=False
    )

    return render_template(
        "question_list.html",
        questions=questions,
        type_length=questions.total,
        # 4 questions can be active at a time, however inactive questions must exist for results.
        # TODO: Find good number for this dilemma
        type_max_count=100,
        main=True
    )


@app.route("/thepollbooth/questions/add", methods=["GET", "POST"])
@oidc.require_login
def add_question():
    form = QuestionForm()
    if form.validate_on_submit():
        new_question = Questions(
            question_id=form.question_id.data,
            content_english=form.content_english.data,
            content_german=form.content_german.data,
            content_french=form.content_french.data,
            content_spanish=form.content_spanish.data,
            content_italian=form.content_italian.data,
            content_dutch=form.content_dutch.data,
            content_portuguese=form.content_portuguese.data,
            content_french_canada=form.content_french_canada.data,
            choice1_english=form.choice1_english.data,
            choice1_german=form.choice1_german.data,
            choice1_french=form.choice1_french.data,
            choice1_spanish=form.choice1_spanish.data,
            choice1_italian=form.choice1_italian.data,
            choice1_dutch=form.choice1_dutch.data,
            choice1_portuguese=form.choice1_portuguese.data,
            choice1_french_canada=form.choice1_french_canada.data,
            choice2_english=form.choice2_english.data,
            choice2_german=form.choice2_german.data,
            choice2_french=form.choice2_french.data,
            choice2_spanish=form.choice2_spanish.data,
            choice2_italian=form.choice2_italian.data,
            choice2_dutch=form.choice2_dutch.data,
            choice2_portuguese=form.choice2_portuguese.data,
            choice2_french_canada=form.choice2_french_canada.data,
            type="w" if form.type.data else "n",  # Map checkbox to "w" or "n"
            date=form.date.data,
            category=form.category.data,
        )

        db.session.add(new_question)
        db.session.commit()

        return redirect(url_for("list_questions"))

    return render_template("question_action.html", form=form, action="Add")


@app.route("/thepollbooth/questions/<question_id>/edit", methods=["GET", "POST"])
@oidc.require_login
def edit_question(question_id: int):
    current_question = Questions.query.filter(Questions.question_id == question_id).first_or_404()
    
    form = QuestionForm(obj=current_question)
    
    if form.validate_on_submit():
        current_question.content_english = form.content_english.data
        current_question.content_german = form.content_german.data
        current_question.content_french = form.content_french.data
        current_question.content_spanish = form.content_spanish.data
        current_question.content_italian = form.content_italian.data
        current_question.content_dutch = form.content_dutch.data
        current_question.content_portuguese = form.content_portuguese.data
        current_question.content_french_canada = form.content_french_canada.data
        current_question.choice1_english = form.choice1_english.data
        current_question.choice1_german = form.choice1_german.data
        current_question.choice1_french = form.choice1_french.data
        current_question.choice1_spanish = form.choice1_spanish.data
        current_question.choice1_italian = form.choice1_italian.data
        current_question.choice1_dutch = form.choice1_dutch.data
        current_question.choice1_portuguese = form.choice1_portuguese.data
        current_question.choice1_french_canada = form.choice1_french_canada.data
        current_question.choice2_english = form.choice2_english.data
        current_question.choice2_german = form.choice2_german.data
        current_question.choice2_french = form.choice2_french.data
        current_question.choice2_spanish = form.choice2_spanish.data
        current_question.choice2_italian = form.choice2_italian.data
        current_question.choice2_dutch = form.choice2_dutch.data
        current_question.choice2_portuguese = form.choice2_portuguese.data
        current_question.choice2_french_canada = form.choice2_french_canada.data
        current_question.type = "w" if form.type.data else "n"
        current_question.date = form.date.data
        current_question.category = form.category.data

        db.session.commit()
        return redirect(url_for("list_questions"))
    
    return render_template("question_action.html", form=form, action="Edit")


@app.route("/thepollbooth//<question_id>/remove", methods=["GET", "POST"])
@oidc.require_login
def remove_question(question_id: int):
    def drop_question():
        db.session.delete(current_question)
        db.session.commit()

        return redirect(url_for("list_questions"))

    current_question = Questions.query.filter(
        Questions.question_id == question_id
    ).first()

    if not current_question:
        return exceptions.NotFound()

    return manage_delete_item(question_id, "question", drop_question)
