# Import necessary libraries
from flask import Flask, request, jsonify
from openai_functions import analyze_image_basic, generate_with_response_model
from prompt_template import anlysis_prompt
from ai_personas import persona_prompts_small
from models import SuggestionsModel
import web_screenshot

# Initialize the Flask app
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
    

@app.route('/analyze_image', methods=['POST'])
def analyze_image_api():
    data = request.get_json()
    image_url = data.get('image_url')

    if not image_url:
        return jsonify({'error': 'No image URL provided'}), 400

    all_persona_results = analyze_image("https://image.thum.io/get/fullpage/"+image_url)

    results_string = '\n'.join(all_persona_results)
    final_prompt = f"Act as a Landing Page Expert Analyzer, please checkout the following feedback from different people about a landing page, extract 7-10 unique suggestions, and return them in a list in JSON format. Feedback: {results_string}"
    # 打印 final_prompt
    print(final_prompt)
    overall_analysis = generate_with_response_model(final_prompt, SuggestionsModel)
    overall_analysis_dict = overall_analysis.result

    return jsonify(overall_analysis_dict)

def analyze_image(image_url):
    all_persona_results = []

    for persona in persona_prompts_small:
        for title, prompt in persona.items():
            persona_prompt = f"{prompt} {anlysis_prompt}"
            result = analyze_image_basic(image_url, persona_prompt)
            all_persona_results.append(result)

    return all_persona_results

if __name__ == '__main__':
    app.run(debug=True)