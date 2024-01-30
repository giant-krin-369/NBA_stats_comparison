import pandas as pd
from NBA_STATS import app
from flask import render_template, request
import nba_api.stats.endpoints
from nba_api.stats.static import teams


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compare', methods=['POST'])
def compare():
    team1 = request.form['team1']
    team2 = request.form['team2']


    # Get team IDs
 #   team1_id = teams.find_team_by_full_name(team1)
  #  team1_id = team1_id[0]['id']

  #  team2_id = teams.find_team_by_full_name(team2)
   # team2_id = team2_id[0]['id']

    # Get the shot location data
    team1_data = nba_api.stats.endpoints.LeagueDashTeamShotLocations(team_id_nullable=team1).get_data_frames()[0]
    team2_data = nba_api.stats.endpoints.LeagueDashTeamShotLocations(team_id_nullable=team2).get_data_frames()[0]
   # team2_data = nba_api.stats.endpoints.LeagueDashTeamShotLocations(team_id="1610612744").get_data_frames()[0]

    # Compare the data
    comparison = pd.concat([team1_data, team2_data], axis=1, keys=[team1, team2])

    return render_template('comparison.html', comparison=comparison.to_html())

if __name__ == '__main__':
    app.run(debug=True)
