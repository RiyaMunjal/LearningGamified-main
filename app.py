from flask import Flask, render_template, request
import numpy as np
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import base64
import io

# Custom modules
import MorseFunctions
import RSA

app = Flask(__name__)


# ? Home Page
@app.route('/')
def home():

    return render_template('home.html')

# ? Kids Games


# Simon Game
@app.route('/simon')
def simon():

    return render_template('simon.html')


# Card Game
@app.route('/cardgame')
def cardgame():

    return render_template('cardgame.html')


# Math Game
@app.route('/mathgame')
def mathgame():

    return render_template('mathgame.html')


# ? Encryption Page
@app.route('/encryption')
def encryption():

    return render_template('encryption.html')


# Morse Code
@app.route('/encryption/morse', methods=['GET', 'POST'])
def morse():

    if request.method == 'POST':

        morse_to_eng_text = request.form.get('morse_to_eng', None)
        eng_to_morse_text = request.form.get('eng_to_morse', None)
        result = {}

        if morse_to_eng_text:
            result["original"] = morse_to_eng_text
            result['morse_to_eng'] = MorseFunctions.morse_to_eng(
                morse_to_eng_text)
        if eng_to_morse_text:
            result["original"] = eng_to_morse_text
            result['eng_to_morse'] = MorseFunctions.eng_to_morse(
                eng_to_morse_text)

        return render_template('morse.html', result=result)

    return render_template('morse.html', result=None)


# RSA
@app.route('/encryption/rsa', methods=['GET', 'POST'])
def rsa():

    if request.method == 'POST':
        originaltext = request.form.get('originaltext', None)

        result = {}
        result["originaltext"] = originaltext

        ciphertext, plaintext, public_key, private_key = RSA.getEncryptedAndDecryptedMessage(
            originaltext)

        result["ciphertext"] = ciphertext
        result["deciphertext"] = plaintext
        result["public_key"] = public_key
        result["private_key"] = private_key

        return render_template('rsa.html', result=result)

    return render_template('rsa.html')


# ML Model
def allowed_file(filename):
    """
    Check if the uploaded file has an allowed extension.
    """
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/mlmodel', methods=['GET', 'POST'])
def mlmodel():

    # Load the model
    model = load_model('static/model/wild_cats_classification_model.h5')

    # Set the default prediction value to None
    prediction = None

    if request.method == 'POST':

        # Get the uploaded file
        f = request.files['fileUpload']

        # If the file exists and is allowed, make a prediction
        if f and allowed_file(f.filename):

            # Load the image and preprocess it for the model
            img = image.load_img(io.BytesIO(f.read()), target_size=(224, 224))
            x = image.img_to_array(img)
            x = np.expand_dims(x, axis=0)
            x = x/255.0

            # Make a prediction using the loaded model
            pred = model.predict(x)
            pred = np.argmax(pred, axis=1)
            labels = {0: 'AFRICAN LEOPARD', 1: 'CARACAL', 2: 'CHEETAH', 3: 'CLOUDED LEOPARD',
                      4: 'JAGUAR', 5: 'LION', 6: 'OCELOT', 7: 'PUMA', 8: 'SNOW LEOPARD', 9: 'TIGER'}

            classification = labels[pred[0]]
            # print(classification)

            # Read the image file and convert it to base64 encoding
            f.seek(0)
            image_file = f.read()
            image_base64 = base64.b64encode(image_file).decode('utf-8')

            # Set the prediction value to be displayed in the HTML template
            prediction = {'image': image_base64,
                          'classification': classification}

    return render_template('mlmodel.html', prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)
