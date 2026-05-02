"""
Aplicação web Flask para geração de senhas complexas.
"""

from flask import Flask, render_template, request, jsonify
from app.main import PasswordGenerator, PasswordSuggester

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def index():
    """Renderiza a página principal."""
    return render_template('index.html')

@app.route('/api/generate', methods=['POST'])
def generate_password():
    """Endpoint para gerar senhas."""
    try:
        data = request.json
        length = int(data.get('length', 12))
        count = int(data.get('count', 3))
        
        # Validação de entrada
        if length < 8 or length > 30:
            return jsonify({'error': 'Comprimento deve estar entre 8 e 30.'}), 400
        
        if count < 1 or count > 10:
            return jsonify({'error': 'Quantidade deve estar entre 1 e 10.'}), 400
        
        # Gerar senhas
        generator = PasswordGenerator()
        suggester = PasswordSuggester(generator)
        passwords = suggester.suggest(length, count=count)
        
        return jsonify({
            'success': True,
            'passwords': passwords,
            'length': length,
            'count': count
        })
    
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': f'Erro inesperado: {str(e)}'}), 500

@app.route('/api/stats', methods=['GET'])
def stats():
    """Endpoint com informações sobre limites."""
    return jsonify({
        'min_length': 8,
        'max_length': 30,
        'max_count': 10,
        'version': '1.0'
    })

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
