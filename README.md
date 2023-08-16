<p align='center'>
<img src ="https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png">
<p>

<h1 align='center'>
 <b>PROYECTO INDIVIDUAL Nº2 - Antonella Nieto</b>
</h1>
 
# <h1 align="center">**`Cryptocurrency Market Data Analytics`**</h1>


<p align='center'>
<img src = 'https://www.bbva.com/wp-content/uploads/2022/03/BBVA-2022-Criptomoneda.jpg' height = 200>
<p>

## **Análisis**

Considerando el objetivo de análisis de la info provista en la API CoinGecko el criterio a considerar fue sobre las 50 monedas con mayor capitalización en el mercado, en la fecha 9 de agosto. 
En esa lista el orden quedó, de mayor a menor, Bitcoin, Ethereum, Tether, BNB, XRP, USD Coin, Lido Staked Ether, Dogecoin, Cardano y Solana.
El valor de capitalización del mercado es el resultado del precio multiplicado por la cantidad en circulación.
Después de filtrar a 10 monedas comparé las monedas según el mayor precio, el menor precio alcanzado y el precio en el período 2015 a fines 2022. 


### **Identificación de outliers**

Con cada atributo numérico visualicé en formato de box plots los outliers de cada uno.
Luego los identifique por atributo calculando el IQR.
En el atributo que denomina el precio más alto alcanzado, está Bitcoin en 69045 dólares. 
En el atributo que denomina el volumen total están las monedas Bitcoin y Tether.
En el atributo que denomina el precio más bajo alcanzado están las monedas Bitcoin y Lido Staked Ether.
En el atributo de cantidad de monedas en circulación está la moneda Dogecoin.
En el atributo capitlización del mercado están las monedas Bitcoin y Ethereum.
En el atributo de precio actual está la moneda de Bitcoin.

## **Conclusiones de los Outliers**

Obteniendo estos resultados, se puede interpretar que Lido Staked Ether es la moneda que dentro de los precios más bajos alcanzados, es el más alto, en 482,90 dólares. Esto registrado en la fecha del 10/11/2021. Siendo su máximo valor alcanzado 4829,57 dólares.
Dado que los datos van desde el 2015, o desde registros después de esa fecha hasta fines de 2022, también aparece como un outlier el valor mínimo alcanzado de Bitcoin, valorado en 67,81 dólares, data en el año 2013. Por lo cuál no es referente para tomar en cuenta en el análisis.
Dogecoin aparece como la moneda con menos circulación en la fecha, con un precio en 0,076 dólares. 


## ***KPI's***
Para el análisis de KPIS tomé en cuenta tres cálculos, la volatilidad del precio, crecimiento de capitalización del mercado y el crecimiento del volumen.
Los datos que se tomaron en cuenta para el análisis son desde principio de año hasta el mes de agosto inclusive.


## ***Conclusiones finales***
Según la volatilidad de precios, una inversión con expectativa de poco crecimiento pero para uso de transacciones diarias, la moneda a recomendar es USD Coin. Con el fin de invertir a un plazo un poco más extenso, pero seguro, la moneda a recomendar es Lido Staked Ether. Su crecimiento  en volúmen no maneja niveles grandes, pero tiene una baja volatilidal en cuánto al precio. Por lo que la hace más segura. Sin embargo, con un poco más de riesgo, la moneda a recomendar es Bitcoin que tiene apenas mejor crecimiento en volumen.
Aunque BNB tiene una baja en capitalización del mercado en el correr del año, en crecimiento de volumen está primera entre las 10 monedas y con la volatibilidad del precio más baja. Haciendola la moneda más rentable según éste análisis.





  
<p align='center'>
<img src ="https://cdn.computerhoy.com/sites/navi.axelspringer.es/public/media/image/2021/11/criptomonedas-vs-acciones-diferencias-incovenientes-cual-mejor-opcion-dinero-2522591.jpg?tf=3840x" height=250>
<p>
