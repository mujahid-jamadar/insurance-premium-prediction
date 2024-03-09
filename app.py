from flask import Flask, request, render_template, jsonify
from src.pipeline.prediction_pipeline import CustomData, PredictPipeline
from src.pipeline.training_pipeline import runpipline

application = Flask(__name__)

app = application
PipelineStatus=False

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/runpipeline')
def runpipeline():
    global PipelineStatus
    
    if not PipelineStatus:
        # Run the pipeline
        run = runpipline()
        PipelineStatus = True
        # Here you can send a response indicating that the pipeline has completed successfully.
        return jsonify({'status': 'success'})
    else:
        # Return a response indicating that the pipeline is already running.
        return jsonify({'status': 'already_running'})



@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('form.html')

    else:
        data = CustomData(
            age=float(request.form.get('age')),
            sex=request.form.get('sex'),
            bmi=float(request.form.get('bmi')),
            children=float(request.form.get('children')),
            smoker=request.form.get('smoker'),
            region=request.form.get('region'),
            
        )
        final_new_data = data.get_data_as_dataframe()
        predict_pipeline = PredictPipeline()
        pred = predict_pipeline.predict(final_new_data)

        results = round(pred[0], 2)

        return render_template('results.html', final_result=results)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
