import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy as np

#Paso 1: Título y subtítulo personalizados
st.markdown(
    """
    <div style="background-color:#1f77b4;padding:10px;border-radius:10px">
        <h1 style="color:white;text-align:center;">Aplicación segundo examen parcial</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# Subtítulo o descripción breve debajo del título
st.markdown(
    """
    <div style="padding:10px;border-radius:10px">
        <h3 style="color:#1f77b4;text-align:center;">Alejandra de la Torre</h3>
    </div>
    """,
    unsafe_allow_html=True
)

# Lista inicial de ETFs con sus nombres de referencia
etf_list = [
    {"name": "AZ China", "possible_symbols": ["FXI", "MCHI", "KWEB"]},
    {"name": "AZ MSCI TAIWAN INDEX FD", "possible_symbols": ["EWT"]},
    {"name": "AZ RUSSELL 2000", "possible_symbols": ["IWM"]},
    {"name": "AZ Brasil", "possible_symbols": ["EWZ"]},
    {"name": "AZ MSCI UNITED KINGDOM", "possible_symbols": ["EWU"]},
    {"name": "AZ DJ US FINANCIAL SECT", "possible_symbols": ["IYF"]},
    {"name": "AZ BRIC", "possible_symbols": ["BKF"]},
    {"name": "AZ MSCI SOUTH KOREA IND", "possible_symbols": ["EWY"]},
    {"name": "AZ BARCLAYS AGGREGATE", "possible_symbols": ["AGG"]},
    {"name": "AZ Mercados Emergentes", "possible_symbols": ["EEM"]},
    {"name": "AZ MSCI EMU", "possible_symbols": ["EZU"]},
    {"name": "AZ FTSE/XINHUA CHINA 25", "possible_symbols": ["FXI"]},
    {"name": "AZ Oro", "possible_symbols": ["GLD"]},
    {"name": "AZ LATIXX MEX CETETRAC", "possible_symbols": ["CTT.MX"]},
    {"name": "AZ QQQ NASDAQ 100", "possible_symbols": ["QQQ"]},
    {"name": "AZ MSCI ASIA EX-JAPAN", "possible_symbols": ["AAXJ"]},
    {"name": "AZ LATIXX MEX M10TRAC", "possible_symbols": ["M10TRAC.MX"]},
    {"name": "AZ BARCLAYS 1-3 YEAR TR", "possible_symbols": ["SHY"]},
    {"name": "AZ MSCI ACWI INDEX FUND", "possible_symbols": ["ACWI"]},
    {"name": "AZ LATIXX MEX M5TRAC", "possible_symbols": ["M5TRAC.MX"]},
    {"name": "AZ SILVER TRUST", "possible_symbols": ["SLV"]},
    {"name": "AZ MSCI HONG KONG INDEX", "possible_symbols": ["EWH"]},
    {"name": "AZ LATIXX MEX UDITRAC", "possible_symbols": ["UDITRAC.MX"]},
    {"name": "AZ SPDR S&P 500 ETF TRUST", "possible_symbols": ["SPY"]},
    {"name": "AZ MSCI JAPAN INDEX FD", "possible_symbols": ["EWJ"]},
    {"name": "AZ BG EUR GOVT BOND 1-3", "possible_symbols": ["IBGE"]},
    {"name": "AZ SPDR DJIA TRUST", "possible_symbols": ["DIA"]},
    {"name": "AZ MSCI FRANCE INDEX FD", "possible_symbols": ["EWQ"]},
    {"name": "AZ DJ US OIL & GAS EXPL", "possible_symbols": ["IEO"]},
    {"name": "AZ VANGUARD EMERGING MARKET ETF", "possible_symbols": ["VWO"]},
    {"name": "AZ MSCI AUSTRALIA INDEX", "possible_symbols": ["EWA"]},
    {"name": "AZ IPC LARGE CAP T R TR", "possible_symbols": ["LCTRT.MX"]},
    {"name": "AZ FINANCIAL SELECT SECTOR SPDR", "possible_symbols": ["XLF"]},
    {"name": "AZ MSCI CANADA", "possible_symbols": ["EWC"]},
    {"name": "AZ S&P LATIN AMERICA 40", "possible_symbols": ["ILF"]},
    {"name": "AZ HEALTH CARE SELECT SECTOR", "possible_symbols": ["XLV"]},
    {"name": "AZ MSCI GERMANY INDEX", "possible_symbols": ["EWG"]},
    {"name": "AZ DJ US HOME CONSTRUCT", "possible_symbols": ["ITB"]}
]

st.markdown(
    """
    <div style="background-color:#e0e0e0;padding:10px;border-radius:8px;margin-top:10px">
        <p style="font-size:18px;font-weight:bold;color:#333;text-align:center;">
            Choose 2 different ETFs to compare
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# Crear lista desplegable de nombres de ETF
etf_names = [etf["name"] for etf in etf_list]
selected_etf1 = st.selectbox("Select the first ETF", etf_names)
selected_etf2 = st.selectbox("Select the second ETF", etf_names)

# Verificar si los ETFs seleccionados son diferentes
if selected_etf1 == selected_etf2:
    st.error("You must select a different ETF.")
else:
    # Encontrar el símbolo correspondiente al ETF seleccionado
    selected_symbol1 = next(etf["possible_symbols"][0] for etf in etf_list if etf["name"] == selected_etf1)
    selected_symbol2 = next(etf["possible_symbols"][0] for etf in etf_list if etf["name"] == selected_etf2)

    # Mostrar el símbolo seleccionado para el primer ETF
    st.markdown(f"<h2 style='font-weight:bold'>{selected_symbol1}</h2>", unsafe_allow_html=True)
    # Obtener y mostrar la descripción del primer ETF
    description1 = yf.Ticker(selected_symbol1).info.get("longBusinessSummary", "Descripción no disponible")
    st.write(f"**Description of {selected_etf1}:**")
    st.markdown(f"<p style='font-size:18px'>{description1}</p>", unsafe_allow_html=True)

    # Mostrar el símbolo seleccionado para el segundo ETF
    st.markdown(f"<h2 style='font-weight:bold'>{selected_symbol2}</h2>", unsafe_allow_html=True)
    # Obtener y mostrar la descripción del segundo ETF
    description2 = yf.Ticker(selected_symbol2).info.get("longBusinessSummary", "Descripción no disponible")
    st.write(f"**Description of {selected_etf2}:**")
    st.markdown(f"<p style='font-size:18px'>{description2}</p>", unsafe_allow_html=True)


    # Crear una selección para el período de tiempo
    period_options = ["10 years", "5 years", "3 years", "1 year", "6 months", "3 months", "1 month"]
    selected_period = st.selectbox("Select the time period for comparison", period_options)

    # Calcular las fechas de inicio y fin según la opción seleccionada
    end_date = datetime.now()
    days_dict = {
        "10 years": 3650,
        "5 years": 1825,
        "3 years": 1095,
        "1 year": 365,
        "6 months": 180,
        "3 months": 90,
        "1 month": 30
    }
    start_date = end_date - timedelta(days=days_dict[selected_period])

# Descargar datos de ambos ETFs y del índice de referencia (MSCI World Index)
    data1 = yf.download(selected_symbol1, start=start_date, end=end_date)
    data2 = yf.download(selected_symbol2, start=start_date, end=end_date)
    data_market = yf.download("URTH", start=start_date, end=end_date)  # Datos del índice MSCI World


    # Graficar los precios de cierre
    plt.figure(figsize=(10, 5))
    plt.plot(data1['Close'], label=f'Close price {selected_etf1}', color='blue')
    plt.plot(data2['Close'], label=f'Close price {selected_etf2}', color='orange')
    plt.title(f'Price comparison between {selected_etf1} and {selected_etf2} ({selected_period})')
    plt.xlabel('Date')
    plt.ylabel('USD price')
    plt.legend()
    plt.grid()
    st.pyplot(plt)

    # Calcular y mostrar rendimientos de ambos ETFs
    initial_price1 = data1['Close'].iloc[0]
    final_price1 = data1['Close'].iloc[-1]
    performance1 = ((final_price1 - initial_price1) / initial_price1) * 100

    initial_price2 = data2['Close'].iloc[0]
    final_price2 = data2['Close'].iloc[-1]
    performance2 = ((final_price2 - initial_price2) / initial_price2) * 100

# Calcular rendimientos de ambos ETFs
initial_price1 = data1['Close'].iloc[0]
final_price1 = data1['Close'].iloc[-1]
performance1 = ((final_price1 - initial_price1) / initial_price1) * 100

initial_price2 = data2['Close'].iloc[0]
final_price2 = data2['Close'].iloc[-1]
performance2 = ((final_price2 - initial_price2) / initial_price2) * 100

# Asegúrate de que performance1 y performance2 sean valores escalares
performance1 = performance1.item()  # Convierte a valor escalar
performance2 = performance2.item()  # Convierte a valor escalar

# Función para mostrar el rendimiento con colores y barra de progreso
def mostrar_rendimiento(etf, performance):
    color = 'green' if performance >= 0 else 'red'
    progreso = int(min(abs(performance), 100))  # Limitar a 100% para el medidor

    # Mostrar el valor y color en formato gauge
    st.markdown(f"<span style='color:{color}; font-size: 20px'><b>Performance of {etf} in the selected period:</b> {performance:.2f}%</span>", unsafe_allow_html=True)
    st.progress(progreso)

# Mostrar el rendimiento de ambos ETFs
mostrar_rendimiento(selected_etf1, performance1)
mostrar_rendimiento(selected_etf2, performance2)

# Calcular los rendimientos diarios
data1['Daily Return'] = data1['Close'].pct_change()
data2['Daily Return'] = data2['Close'].pct_change()

# Calcular la volatilidad diaria como la desviación estándar de los rendimientos diarios
volatility1 = data1['Daily Return'].std() * 100  # en porcentaje
volatility2 = data2['Daily Return'].std() * 100  # en porcentaje

# Mostrar la volatilidad en Streamlit
st.metric(label=f"Daily Volatility of {selected_etf1}", value=f"{volatility1:.2f}%")
st.metric(label=f"Daily Volatility of {selected_etf2}", value=f"{volatility2:.2f}%")

# Asegurarnos de que data1, data2 y data_market tengan el mismo índice y eliminar datos faltantes
aligned_data1 = pd.concat([data1['Close'], data_market['Close']], axis=1, keys=['ETF1', 'Market']).dropna()
aligned_data2 = pd.concat([data2['Close'], data_market['Close']], axis=1, keys=['ETF2', 'Market']).dropna()

# Calcular los rendimientos diarios de ambos conjuntos de datos para cada ETF
aligned_data1['ETF1 Returns'] = aligned_data1['ETF1'].pct_change()
aligned_data1['Market Returns'] = aligned_data1['Market'].pct_change()

aligned_data2['ETF2 Returns'] = aligned_data2['ETF2'].pct_change()
aligned_data2['Market Returns'] = aligned_data2['Market'].pct_change()

# Calcular la beta para el primer ETF
cov_matrix1 = aligned_data1[['ETF1 Returns', 'Market Returns']].cov()
beta1 = cov_matrix1.loc['ETF1 Returns', 'Market Returns'] / cov_matrix1.loc['Market Returns', 'Market Returns']

# Calcular la beta para el segundo ETF
cov_matrix2 = aligned_data2[['ETF2 Returns', 'Market Returns']].cov()
beta2 = cov_matrix2.loc['ETF2 Returns', 'Market Returns'] / cov_matrix2.loc['Market Returns', 'Market Returns']

# Convertir beta1 y beta2 a escalar en caso de que sean Series
if isinstance(beta1, pd.Series):
    beta1 = beta1.iloc[0]
if isinstance(beta2, pd.Series):
    beta2 = beta2.iloc[0]

# Calcular la máxima caída de precio en términos monetarios para cada ETF
max_drawdown1 = aligned_data1['ETF1'].max() - aligned_data1['ETF1'].min()
max_drawdown2 = aligned_data2['ETF2'].max() - aligned_data2['ETF2'].min()

# Convertir max_drawdown1 y max_drawdown2 a escalar en caso de que sean Series
if isinstance(max_drawdown1, pd.Series):
    max_drawdown1 = max_drawdown1.iloc[0]
if isinstance(max_drawdown2, pd.Series):
    max_drawdown2 = max_drawdown2.iloc[0]

# Función para asignar etiqueta de riesgo basado en el valor de beta
def riesgo_label(beta):
    if beta >= 1.5:
        return "🔴 Alto Riesgo"
    elif beta >= 1.0:
        return "🟠 Moderado"
    else:
        return "🟢 Bajo Riesgo"

# Encabezado para separar la sección de riesgo
st.markdown("### **Análisis de Riesgo y Máxima Caída para los ETFs seleccionados**")

# Mostrar Beta y Máxima Caída para el primer ETF
st.markdown(f"#### {selected_etf1}")
st.write(f"**Beta**: {beta1:.2f} - {riesgo_label(beta1)}")
st.write(f"**Máxima Caída en términos monetarios:** ${max_drawdown1:.2f}")

# Espacio para separar los dos ETFs
st.markdown("---")

# Mostrar Beta y Máxima Caída para el segundo ETF
st.markdown(f"#### {selected_etf2}")
st.write(f"**Beta**: {beta2:.2f} - {riesgo_label(beta2)}")
st.write(f"**Máxima Caída en términos monetarios:** ${max_drawdown2:.2f}")

#Escribir la inversión
st.markdown(
    """
    <div style="background-color:#e0e0e0;padding:10px;border-radius:8px;margin-top:10px">
        <p style="font-size:18px;font-weight:bold;color:#333;text-align:center;">
            Write the amount you would like to invest in each ETF
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# Cuadros para ingresar la cantidad a invertir en cada ETF
investment_amount1 = st.number_input(f"Ingrese la cantidad que desea invertir en {selected_etf1}:", min_value=0.0, step=100.0)
investment_amount2 = st.number_input(f"Ingrese la cantidad que desea invertir en {selected_etf2}:", min_value=0.0, step=100.0)

# Calcular el retorno esperado para cada inversión individualmente
if investment_amount1 > 0 or investment_amount2 > 0:
    # Cálculo del retorno para cada ETF usando el rendimiento
    gain1 = investment_amount1 * (performance1 / 100)
    gain2 = investment_amount2 * (performance2 / 100)
    
    # Monto total esperado para cada inversión
    total1 = investment_amount1 + gain1
    total2 = investment_amount2 + gain2

    # Calcular el total combinado de ambas inversiones
    total_combined = total1 + total2

    # Crear un DataFrame para mostrar los resultados en una tabla
    results_df = pd.DataFrame({
        "ETF": [selected_etf1, selected_etf2],
        "Rendimiento (%)": [f"{performance1:.2f}%", f"{performance2:.2f}%"],
        "Retorno Esperado ($)": [f"${gain1:.2f}", f"${gain2:.2f}"],
        "Monto Final Esperado ($)": [f"${total1:.2f}", f"${total2:.2f}"]
    })

    st.write("### Resultados de la Inversión por ETF")
    st.table(results_df)

    # Mostrar el total combinado con estilo destacado
    st.markdown(
        f"<div style='text-align:center; font-size:22px; font-weight:bold; color:#2E8B57;'>"
        f"Total combinado de la inversión esperada: ${total_combined:.2f}"
        f"</div>", 
        unsafe_allow_html=True
    )
else:
    st.write("Ingrese cantidades válidas para calcular el retorno de la inversión.")