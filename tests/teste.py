import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from focosimples.main import gerar_cronograma

def test_distribuicao_tempo_exata():
    materias = [
        {"nome": "Matematica", "prioridade": 5},
        {"nome": "Portugues", "prioridade": 5}
    ]
    resultado = gerar_cronograma(2, materias)
    assert resultado[0]['minutos'] == 60
    assert resultado[1]['minutos'] == 60

def test_cronograma_vazio():
    assert gerar_cronograma(2, []) == []
