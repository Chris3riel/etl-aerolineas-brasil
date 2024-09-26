import pytest
import pandas as pd
from etl import extract, transform, load

@pytest.fixture
def sample_data():
    data = {
        'Voos': ['V001', 'V002'],
        'Companhia.Aerea': ['Airline1', 'Airline2'],
        'Codigo.Tipo.Linha': ['Tipo1', 'Tipo2'],
        'Partida.Prevista': ['2023-01-01 08:00', '2023-01-01 09:00'],
        'Partida.Real': ['2023-01-01 08:05', '2023-01-01 09:10'],
        'Chegada.Prevista': ['2023-01-01 10:00', '2023-01-01 11:00'],
        'Chegada.Real': ['2023-01-01 10:05', '2023-01-01 11:10'],
        'Situacao.Voo': ['On-time', 'Delayed'],
        'Codigo.Justificativa': ['Just1', 'Just2'],
        'Aeroporto.Origem': ['Aero1', 'Aero2'],
        'Cidade.Origem': ['City1', 'City2'],
        'Estado.Origem': ['State1', 'State2'],
        'Pais.Origem': ['Country1', 'Country2'],
        'Aeroporto.Destino': ['Dest1', 'Dest2'],
        'Cidade.Destino': ['CityDest1', 'CityDest2'],
        'Estado.Destino': ['StateDest1', 'StateDest2'],
        'Pais.Destino': ['CountryDest1', 'CountryDest2'],
        'LongDest': [12.34, 56.78],
        'LatDest': [98.76, 54.32],
        'LongOrig': [21.43, 65.87],
        'LatOrig': [87.65, 45.23]
    }
    return pd.DataFrame(data)

def test_extract(tmp_path):
    # Crear un archivo CSV temporal
    file_path = tmp_path / "test.csv"
    sample_data = {
        'Voos': ['V001', 'V002'],
        'Companhia.Aerea': ['Airline1', 'Airline2'],
        'Codigo.Tipo.Linha': ['Tipo1', 'Tipo2'],
        'Partida.Prevista ': ['2023-01-01 08:00', '2023-01-01 09:00'],
        'Partida.Real': ['2023-01-01 08:05', '2023-01-01 09:10'],
        'Chegada.Prevista': ['2023-01-01 10:00', '2023-01-01 11:00'],
        'Chegada.Real': ['2023-01-01 10:05', '2023-01-01 11:10'],
        'Situacao.Voo': ['On-time', 'Delayed'],
        'Codigo.Justificativa': ['Just1', 'Just2'],
        'Aeroporto.Origem': ['Aero1', 'Aero2'],
        'Cidade.Origem': ['City1', 'City2'],
        'Estado.Origem': ['State1', 'State2'],
        'Pais.Origem': ['Country1', 'Country2'],
        'Aeroporto.Destino': ['Dest1', 'Dest2'],
        'Cidade.Destino': ['CityDest1', 'CityDest2'],
        'Estado.Destino': ['StateDest1', 'StateDest2'],
        'Pais.Destino': ['CountryDest1', 'CountryDest2'],
        'LongDest': [12.34, 56.78],
        'LatDest': [98.76, 54.32],
        'LongOrig': [21.43, 65.87],
        'LatOrig': [87.65, 45.23]
    }
    pd.DataFrame(sample_data).to_csv(file_path, index=False)
    
    data = extract(file_path)
    assert isinstance(data, pd.DataFrame)
    assert len(data) == 2

def test_transform(sample_data):
    transformed_data = transform(sample_data)
    assert transformed_data['Partida.Prevista'].dtype == 'datetime64[ns]'
    assert transformed_data['Partida.Real'].dtype == 'datetime64[ns]'
    assert transformed_data['Chegada.Prevista'].dtype == 'datetime64[ns]'
    assert transformed_data['Chegada.Real'].dtype == 'datetime64[ns]'
    assert 'Companhia_Aerea' in transformed_data.columns

def test_load(sample_data):
    result = load(sample_data)
    assert result == True