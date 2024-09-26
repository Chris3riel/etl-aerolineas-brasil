import pandas as pd

def extract(file_path):
    data = pd.read_csv(file_path)
    return data

def transform(data):
    # convertir las fechas a un formato datetime
    data['Partida.Prevista'] = pd.to_datetime(data['Partida.Prevista'])
    data['Partida.Real'] = pd.to_datetime(data['Partida.Real'])
    data['Chegada.Prevista'] = pd.to_datetime(data['Chegada.Prevista'])
    data['Chegada.Real'] = pd.to_datetime(data['Chegada.Real'])
    
    # Renombrar algunas columnas para mayor claridad
    data = data.rename(columns={
        'Companhia.Aerea': 'Companhia_Aerea',
        'Codigo.Tipo.Linha': 'Codigo_Tipo_Linha',
        'Situacao.Voo': 'Situacao_Voo',
        'Codigo.Justificativa': 'Codigo_Justificativa',
        'Aeroporto.Origem': 'Aeroporto_Origem',
        'Cidade.Origem': 'Cidade_Origem',
        'Estado.Origem': 'Estado_Origem',
        'Pais.Origem': 'Pais_Origem',
        'Aeroporto.Destino': 'Aeroporto_Destino',
        'Cidade.Destino': 'Cidade_Destino',
        'Estado.Destino': 'Estado_Destino',
        'Pais.Destino': 'Pais_Destino',
        'LongDest': 'Longitude_Destino',
        'LatDest': 'Latitude_Destino',
        'LongOrig': 'Longitude_Origem',
        'LatOrig': 'Latitude_Origem'
    })
    
    return data

def load(data):
    # Simulación de la carga de datos
    print("Loading data...")
    print(data.head())
    return True