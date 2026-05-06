

LANGUAGES = {
    "English": {
        "title": "DILUTION EYE",
        "tagline": "Share structure analysis",
        "input_label": "Search Ticker or ISIN",
        "input_placeholder": "(GOOG, AAPL, NVDA, TSLA...)",
        "btn_analyze": "Analyze",
        "date": "Date",
        "chart_y_label": "Shares Outstanding",

        # other tickers
        "error_empty": "⚠️ Please enter a Ticker or ISIN before analyzing.",
        "error_not_found": "Ticker not found. Please check the symbol and try again.",
        "loading_after_research": "Analyzing...",
        "rate_limit": "Yahoo Finance is temporarily unavailable (Rate Limit). Please try again in a few minutes.",

        "kpi_shares": "Total Shares",
        "kpi_change": "Last Year Change",
        "kpi_status": "Current Status",
        "chart_title": "Shares Outstanding evolution",
        "alert_title": "Log Alerts",
        "footer_disclaimer": "⚠️ The information provided is for informational purposes only and does not constitute financial advice. The author assumes no responsibility for decisions based on this data.",
        "donate_title": "Support Dilution Eye",
        "donate_sub": "Click the address to copy and donate Bitcoin",
        "address_copied": "Copied!"
    },
    "Italiano": {
        "title": "DILUTION EYE",
        "tagline": "Analisi della struttura azionaria",
        "input_label": "Cerca Ticker o ISIN",
        "input_placeholder": "(GOOG, AAPL, NVDA, TSLA...)",
        "btn_analyze": "Analizza",
        "date": "Data",
        "chart_y_label": "Azioni in Circolazione",


        #other tickers
        "error_empty": "⚠️ Per favore, inserisci un Ticker o un ISIN prima di analizzare.",
        "error_not_found": "Ticker non trovato. Controlla il codice e riprova.",
        "loading_after_research": "Analisi in corso...",
        "rate_limit": " Yahoo Finance è temporaneamente non disponibile (Rate Limit). Riprova tra qualche minuto.",

        "kpi_shares": "Azioni Totali",
        "kpi_change": "Var. Ultimo Anno",
        "kpi_status": "Stato corrente",
        "chart_title": "Evoluzione del numero di azioni",
        "alert_title": "Log Alert",
        "footer_disclaimer": "⚠️ Le informazioni fornite hanno scopo puramente informativo e non costituiscono consigli finanziari. L'autore non si assume responsabilità per decisioni basate su questi dati.",
        "donate_title": "Supporta Dilution Eye",
        "donate_sub": "Clicca sull'indirizzo per copiare e donare in Bitcoin",
        "address_copied": "Copiato!"
    },
    "Español": {
        "title": "DILUTION EYE",
        "tagline": "Análisis de la estructura accionaria",
        "input_label": "Buscar Ticker o ISIN",
        "input_placeholder": "(GOOG, AAPL, NVDA, TSLA...)",
        "btn_analyze": "Analizar",
        "date": "Fecha",
        "chart_y_label": "Acciones en circulación",


        # other tickers
        "error_empty": "⚠️ Por favor, ingrese un Ticker o ISIN antes de analizar.",
        "error_not_found": "Ticker no encontrado. Compruebe el símbolo e inténtelo de nuevo.",
        "loading_after_research": "Análisis en curso...",
        "rate_limit": "Yahoo Finance no está disponible temporalmente (Límite de peticiones). Inténtelo de nuevo en unos minutos.",

        "kpi_shares": "Acciones Totales",
        "kpi_change": "Var. Último Año",
        "kpi_status": "Estado actual",
        "chart_title": "Evolución del número de acciones",
        "alert_title": "Registro Alertas",
        "footer_disclaimer": "⚠️ La información proporcionada es solo para fines informativos y no constituye asesoramiento financiero. El autor no asume responsabilidad por las decisiones basadas en estos datos.",
        "donate_title": "Apoya a Dilution Eye",
        "donate_sub": "Haga clic en la dirección para copiar y donar en Bitcoin",
        "address_copied": "¡Copiado!"
    },
    "Français": {
        "title": "DILUTION EYE",
        "tagline": "Analyse de la structure d'actionnariat",
        "input_label": "Chercher Ticker ou ISIN",
        "input_placeholder": "(GOOG, AAPL, NVDA, TSLA...)",
        "btn_analyze": "Analyser",
        "date": "Date",
        "chart_y_label": "Actions en circulation",


        # other tickers
        "error_empty": "⚠️ Veuillez saisir un Ticker ou un ISIN avant d'analyser.",
        "error_not_found": "Ticker introuvable. Veuillez vérifier le symbole et réessayer.",
        "loading_after_research": "Analyse en cours...",
        "rate_limit": "Yahoo Finance est temporairement indisponible (Limite de requêtes). Veuillez réessayer dans quelques minutes.",

        "kpi_shares": "Actions Totales",
        "kpi_change": "Var. Dernière Année",
        "kpi_status": "État actuel",
        "chart_title": "Évolution du nombre d'actions",
        "alert_title": "Journal alertes",
        "footer_disclaimer": "⚠️ Les informations fournies le sont à titre informatif uniquement et ne constituent pas un conseil financier. L'auteur n'assume aucune responsabilité pour les décisions basées sur ces données.",
        "donate_title": "Soutenir Dilution Eye",
        "donate_sub": "Cliquez sur l'adresse pour copier et faire un don en Bitcoin",
        "address_copied": "Copié !"
    }
}

# FAQ
FAQ = {
    "English": {
        "title": "F.A.Q.",
        "q1": "Where does the data come from?",
        "a1": "All data comes from Yahoo Finance via the yfinance library. For each ticker or ISIN, two historical series are downloaded: the number of outstanding shares over time and the history of stock splits with their respective dates and multipliers.",
        "q2": "What are stock splits and why do they need to be handled?",
        "a2": "A split is when a company divides its shares (e.g., 2-for-1). Without normalization, a company doing a 2-for-1 split would appear to have diluted shareholders by 100%, which is false. The shareholder's value remains unchanged. The program corrects this mathematical artifact by recalculating the entire historical series based on subsequent splits.",
        "q3": "What does data 'normalization' mean?",
        "a3": "It means retroactively adjusting historical share counts as if all splits had already occurred. In practice: if there was a x2 split in 2020, all shares counted before 2020 are multiplied by 2. This creates a consistent and comparable timeline.",
        "q4": "How is year-over-year dilution calculated?",
        "a4": "Once the historical series is normalized, the program extracts the final data point of each calendar year and applies the formula: \n\n$$\\frac{\\text{Current Year Shares} - \\text{Previous Year Shares}}{\\text{Previous Year Shares}} \\times 100$$ \n\nThe result is the net percentage change, already adjusted for splits.",
        "q5": "What are Alerts?",
        "a5": "They are automatic warnings that highlight historical stock situations based on YoY (Year-over-Year) percentages.",
        "q6": "What are the Alerts and when are they triggered?",
        "a6": "🟢 **POSITIVE** (<= 0%): Stock Buyback. The company hasn't issued shares or has bought them back. Your 'slice of the pie' gets bigger.\n\n"
              "⚪ **STABLE** (0% to 5%): Neutral / Normal. A physiological micro-dilution, often used for employee stock options.\n\n"
              "🟡 **WARNING** (5% to 10%): Significant Dilution. The company is issuing new shares for funding, reducing your stake.\n\n"
              "🚩 **DILUTING** (> 10%): Severe Dilution. The company is flooding the market with new shares. Often a sign of desperate need for liquidity.\n\n"
              "🚨 **Special Alert**: Reverse Split. Flagged in red regardless of percentage. The company merges shares to artificially raise a collapsed stock price.",
        "q7": "Can I predict future dilutions?",
        "a7": "No. Dilution Eye cannot predict future dilutions; the tool only analyzes consolidated historical data.",
        "q8": "Can I search for any publicly traded company?",
        "a8": "Yes, for any ticker or ISIN available on Yahoo Finance, which covers the vast majority of global stock exchanges.",
        "q9": "What are the limitations of Dilution Eye?",
        "a9": "The main limits are: \n\n 1) Reliance on Yahoo Finance (if data on their servers is incomplete or incorrect, the results will be too). \n\n 2) Dilution from employee stock options is difficult to isolate purely from historical outstanding shares data.",
        "q10": "Can I search for ETFs or other financial instruments?",
        "a10": "No. The search is indexed for stocks only.",
        "q11": "Why does searching for ENI, ISP, or other companies return no results?",
        "a11": "Since they are listed on multiple exchanges, you must add the **exchange suffix** of the primary market (e.g., .MI for Milan) to the ticker. Alternatively, enter the ISIN for a more precise result."
    },
    "Italiano": {
        "title": "F.A.Q.",
        "q1": "Da dove provengono i dati?",
        "a1": "Tutti i dati provengono da Yahoo Finance tramite la libreria yfinance. Per ogni ticker o ISIN vengono scaricate due serie storiche: il numero di azioni in circolazione nel tempo e la storia degli split azionari con le relative date e moltiplicatori.",
        "q2": "Cosa sono gli split azionari e perché è necessario gestirli?",
        "a2": "Uno split è quando un'azienda divide le sue azioni (es. 2-for-1: ogni azione diventa due). Senza una normalizzazione, un'azienda che fa uno split 2-a-1 sembrerebbe aver diluito del 100% gli azionisti, il che è falso. Il valore per l'azionista resta invariato. Il programma corregge questo artefatto matematico ricalcolando tutta la serie storica in base agli split successivi.",
        "q3": "Cosa significa 'normalizzazione' dei dati?",
        "a3": "Significa aggiustare retroattivamente i conteggi storici delle azioni come se tutti gli split fossero già avvenuti. In pratica: se c'è stato uno split x2 nel 2020, tutte le azioni conteggiate prima del 2020 vengono moltiplicate per 2. Così si ottiene una linea temporale coerente e comparabile nel tempo.",
        "q4": "Come viene calcolata la diluizione anno per anno?",
        "a4": "Una volta normalizzata la serie storica, il programma estrae il dato finale di ogni anno (solare) e applica la formula: \n\n$$\\frac{\\text{Azioni Anno Corrente} - \\text{Azioni Anno Precedente}}{\\text{Azioni Anno Precedente}} \\times 100$$ \n\nIl risultato è la variazione percentuale netta, già corretta per gli split.",
        "q5": "Cosa sono gli Alerts?",
        "a5": "Sono avvisi automatici che segnalano situazioni storiche sulle azioni, basate sulle percentuali YoY (Year-over-Year).",
        "q6": "Quali sono e quando scattano gli Alerts?",
        "a6": "🟢 **POSITIVE** (<= 0%): Stock Buyback. L'azienda non ha emesso azioni o le ha ricomprate per distruggerle. La tua 'fetta di torta' diventa più grande.\n\n"
              "⚪ **STABLE** (Tra 0% e 5%): Neutrale / Fisiologico. Una micro-diluizione del tutto normale, spesso usata per compensare i dipendenti.\n\n"
              "🟡 **WARNING** (Tra 5% e 10%): Diluizione Significativa. L'azienda sta emettendo nuove azioni per finanziarsi, riducendo la tua quota.\n\n"
              "🚩 **DILUTING** (> 10%): Diluizione Grave. L'azienda sta inondando il mercato di nuove azioni. Spesso sintomo di necessità di liquidità.\n\n"
              "🚨 **Alert Speciale**: Reverse Split. Segnalato in rosso a prescindere. L'azienda accorpa le azioni per alzare artificialmente il prezzo crollato in borsa.",
        "q7": "Posso prevedere diluizioni future?",
        "a7": "No. Con Dilution Eye non puoi prevedere eventuali diluizioni future, il tool analizza solo lo storico consolidato.",
        "q8": "Si può cercare qualsiasi azienda quotata in borsa?",
        "a8": "Sì, per qualsiasi ticker o ISIN disponibile su Yahoo Finance, che copre la grande maggioranza delle borse mondiali.",
        "q9": "Quali sono i limiti di Dilution Eye?",
        "a9": "I principali limiti sono due: \n\n 1) Dipendenza da Yahoo Finance (se i dati sul loro server sono incompleti o errati, lo saranno anche i risultati). \n\n 2) La diluizione derivante da stock option o compensi ai dipendenti è difficile da isolare dai soli dati storici globali.",
        "q10": "Posso cercare ETF o altri strumenti finanziari?",
        "a10": "No. La ricerca è indicizzata solo alle azioni.",
        "q11": "Perché se cerco ENI, ISP o altre società non restituisce nulla?",
        "a11": "Poiché sono quotate su più mercati, è necessario aggiungere il **suffisso della borsa di riferimento** (es. .MI per Milano) al ticker. In alternativa, inserisci l'ISIN per un risultato più preciso."
    },
    "Español": {
        "title": "F.A.Q.",
        "q1": "¿De dónde provienen los datos?",
        "a1": "Todos los datos provienen de Yahoo Finance a través de la biblioteca yfinance. Para cada ticker o ISIN, se descargan dos series históricas: el número de acciones en circulación a lo largo del tiempo y el historial de splits con sus respectivas fechas y multiplicadores.",
        "q2": "¿Qué son los splits de acciones y por qué es necesario gestionarlos?",
        "a2": "Un split ocurre cuando una empresa divide sus acciones (ej. 2 por 1). Sin normalización, una empresa que hace un split 2 a 1 parecería haber diluido a los accionistas en un 100%, lo cual es falso. El valor para el accionista se mantiene sin cambios. El programa corrige este artefacto matemático recalculando toda la serie histórica en función de los splits posteriores.",
        "q3": "¿Qué significa la 'normalización' de datos?",
        "a3": "Significa ajustar retroactivamente los recuentos históricos de acciones como si todos los splits ya hubieran ocurrido. En la práctica: si hubo un split x2 en 2020, todas las acciones contabilizadas antes de 2020 se multiplican por 2. Esto crea una línea de tiempo coherente y comparable.",
        "q4": "¿Cómo se calcula la dilución año tras año?",
        "a4": "Una vez normalizada la serie histórica, el programa extrae el dato final de cada año natural y aplica la fórmula: \n\n$$\\frac{\\text{Acciones Año Actual} - \\text{Acciones Año Anterior}}{\\text{Acciones Año Anterior}} \\times 100$$ \n\nEl resultado es la variación porcentual neta, ya corregida por los splits.",
        "q5": "¿Qué son las Alertas?",
        "a5": "Son avisos automáticos que señalan situaciones históricas sobre las acciones, basadas en porcentajes interanuales (YoY).",
        "q6": "¿Cuáles son las Alertas y cuándo se activan?",
        "a6": "🟢 **POSITIVE** (<= 0%): Stock Buyback. La empresa no ha emitido acciones o las ha recomprado. Tu 'parte del pastel' se hace más grande.\n\n"
              "⚪ **STABLE** (0% a 5%): Neutral / Fisiológico. Una micro-dilución normal, a menudo usada para compensar empleados.\n\n"
              "🟡 **WARNING** (5% a 10%): Dilución Significativa. La empresa está emitiendo nuevas acciones para financiarse.\n\n"
              "🚩 **DILUTING** (> 10%): Dilución Grave. La empresa está inundando el mercado con nuevas acciones.\n\n"
              "🚨 **Alerta Especial**: Reverse Split. Señalado en rojo independientemente del porcentaje. La empresa agrupa acciones para elevar artificialmente un precio colapsado.",
        "q7": "¿Puedo predecir futuras diluciones?",
        "a7": "No. Dilution Eye no puede predecir futuras diluciones; la herramienta solo analiza el historial consolidado.",
        "q8": "¿Puedo buscar cualquier empresa que cotice en bolsa?",
        "a8": "Sí, para cualquier ticker o ISIN disponible en Yahoo Finance, que cubre la gran mayoría de las bolsas mundiales.",
        "q9": "What are the limitations of Dilution Eye?",
        "a9": "Los límites principales son: \n\n 1) Dependencia de Yahoo Finance (si los datos en sus servidores están incompletos o son incorrectos, los resultados también lo serán). \n\n 2) La dilución derivada de opciones sobre acciones para empleados es difícil de aislar solo con datos históricos de acciones en circulación.",
        "q10": "¿Puedo buscar ETFs u otros instrumentos financieros?",
        "a10": "No. La búsqueda está indexada solo para acciones.",
        "q11": "¿Por qué si busco ENI, ISP u otras empresas no devuelve nada?",
        "a11": "Debido a que cotizan en varios mercados, es necesario añadir el **sufijo de la bolsa de referencia** (ej. .MI para Milán) al ticker. Alternativamente, introduzca el ISIN para un resultado más preciso."
    },
    "Français": {
        "title": "F.A.Q.",
        "q1": "D'où proviennent les données ?",
        "a1": "Toutes les données proviennent de Yahoo Finance via la bibliothèque yfinance. Pour chaque ticker ou ISIN, deux séries historiques sont téléchargées : le nombre d'actions en circulation au fil du temps et l'historique des fractionnements (splits) avec leurs dates et multiplicateurs respectifs.",
        "q2": "Que sont les fractionnements d'actions et pourquoi faut-il les gérer ?",
        "a2": "Un split se produit lorsqu'une entreprise divise ses actions (ex. 2 pour 1). Sans normalisation, une entreprise effectuant un split 2 pour 1 semblerait avoir dilué ses actionnaires de 100 %, ce qui est faux. La valeur pour l'actionnaire reste inchangée. Le programme corrige cet artefact mathématique en recalculant toute la série historique en fonction des splits ultérieurs.",
        "q3": "Que signifie la 'normalisation' des données ?",
        "a3": "Cela signifie ajuster rétroactivement les décomptes historiques d'actions comme si tous les splits avaient déjà eu lieu. En pratique : s'il y a eu un split x2 en 2020, toutes les actions comptabilisées avant 2020 sont multipliées par 2. Cela crée une chronologie cohérente et comparable.",
        "q4": "How is year-over-year dilution calculated?",
        "a4": "Une fois la série historique normalisée, le programme extrait la donnée finale de chaque année civile et applique la formule : \n\n$$\\frac{\\text{Actions Année Courante} - \\text{Actions Année Précédente}}{\\text{Actions Année Précédente}} \\times 100$$ \n\nLe résultat est la variation en pourcentage net, déjà corrigée des splits.",
        "q5": "Que sont les Alertes ?",
        "a5": "Ce sont des avertissements automatiques signalant des situations historiques sur les actions, basées sur des pourcentages annuels (YoY).",
        "q6": "Quelles sont les Alertes et quand se déclenchent-elles ?",
        "a6": "🟢 **POSITIVE** (<= 0 %) : Rachat d'actions (Buyback). L'entreprise n'a pas émis d'actions ou les a rachetées.\n\n"
              "⚪ **STABLE** (0 % à 5 %) : Neutre / Physiologique. Une micro-dilution normale, souvent utilisée pour rémunérer les employés.\n\n"
              "🟡 **WARNING** (5 % à 10 %) : Dilution Significative. L'entreprise émet de nouvelles actions.\n\n"
              "🚩 **DILUTING** (> 10 %) : Dilution Sévère. L'entreprise inonde le marché de nouvelles actions.\n\n"
              "🚨 **Alerte Spéciale** : Regroupement d'actions (Reverse Split). Signalé en rouge quel que soit le pourcentage. L'entreprise regroupe des actions per augmenter artificiellement le prix.",
        "q7": "Puis-je prévoir les dilutions futures ?",
        "a7": "Non. Dilution Eye ne peut pas prédire les éventuelles dilutions futures ; l'outil n'analyse que l'historique consolidé.",
        "q8": "Peut-on rechercher n'importe quelle entreprise cotée en bourse ?",
        "a8": "Oui, pour tout ticker ou ISIN disponible sur Yahoo Finance, qui couvre la grande majorité des bourses mondiales.",
        "q9": "What are the limitations of Dilution Eye?",
        "a9": "Les principales limites sont : \n\n 1) Dépendance à Yahoo Finance (si les données sur leurs serveurs sont incomplètes ou erronées, les résultats le seront aussi). \n\n 2) La dilution due aux stock-options pour les employés est difficile à isoler des seules données historiques des actions en circulation.",
        "q10": "Puis-je rechercher des ETF ou d'autres instruments financiers ?",
        "a10": "Non. La recherche est indexée uniquement pour les actions.",
        "q11": "Pourquoi la recherche d'ENI, ISP ou d'autres sociétés ne donne-t-elle aucun résultat ?",
        "a11": "Comme elles sont cotées sur plusieurs marchés, il est nécessaire d'ajouter l'**extension de la bourse de référence** (ex. .MI pour Milan) au ticker. Alternativement, saisissez l'ISIN pour un résultat plus précis."
    }
}