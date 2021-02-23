from flask import Flask, render_template, request, session

from stories import Story, story1, story2, story3
stories =[story1,story2,story3]

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/story')
def story_display():
    t = int(request.args.get('t'))
    result = stories[t].generate(request.args)
    return render_template('story.html',story = result)

@app.route('/template')
def story_template():
    t = int(request.args.get('t'))
    prompts = stories[t].prompts
    return render_template('template.html', prompts =prompts,t=t)
