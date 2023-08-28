#  Materiale utile


## ------ CONVERSIONE colonna data a datetime64 -----------------------------

# OPZIONE 1

# Prova a convertire utilizzando il formato completo prima
df['Date and time (UTC)'] = pd.to_datetime(df['Date and time (UTC)'], format='%d %B %H:%M', errors='coerce', dayfirst= True, exact = True)

# Ora, per le date che non sono state convertite, prova un formato senza l'orario
df.loc[df['Date and time (UTC)'].isna(), 'Date and time (UTC)'] = pd.to_datetime(df.loc[df['Date and time (UTC)'].isna(), 'Date and time (UTC)'], format='%d %B', errors='coerce')

# Infine, prova un formato senza il giorno del mese
df.loc[df['Date and time (UTC)'].isna(), 'Date and time (UTC)'] = pd.to_datetime(df.loc[df['Date and time (UTC)'].isna(), 'Date and time (UTC)'], format='%B', errors='coerce')


# OPZIONE 2

# Conversion with complete format "day month time", coerce sets errors as NaT (not a time)
df['Date and time (UTC)'] = pd.to_datetime(df['Date and time (UTC)'], format='%d %B %H:%M', errors='ignore', dayfirst=True)

# Conversion of NaT with "day month" format
df['Date and time (UTC)'] = pd.to_datetime(df['Date and time (UTC)'], format='%d %B', errors='ignore', dayfirst=True, infer_datetime_format = True)

# Conversion with just the month, "month" format
df['Date and time (UTC)'] = pd.to_datetime(df['Date and time (UTC)'], format='%B', errors='ignore', dayfirst=True, infer_datetime_format = True)



## PALETTE GRafico a barre

import plotly.express as px
from plotly.colors import n_colors

# Genera una palette di colori
palette = n_colors('rgb(0, 0, 200)', 'rgb(200, 0, 0)', len(filtered_value_counts.index), colortype='rgb')

fig = px.bar(x=filtered_value_counts.index, 
             y=filtered_value_counts.values, 
             labels={'x':'Function', 'y':'Count'},
             color=filtered_value_counts.index, 
             color_discrete_sequence=palette)

fig.show()
