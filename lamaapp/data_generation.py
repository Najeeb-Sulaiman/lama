import random
from datetime import datetime, timedelta

# Helper function to generate random datetime
def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

# Generate random data
competition = ['NPFL']
position = ['Goalkeeper','Defender', 'Midfielder','Forward']
#player = [('Nduka Junior', 'Defender'), ('Ahmed Akinyele','Defender'), ('Jide Fatokun', 'Midfielder'), ('Ismaila Sodiq','Defender'), ('Stanley Joseph', 'Defender'),('Olamilekan Adedayo','Midfielder'),('Hadi Haruna','Midfielder'),('Olamilekan Adams', 'Forward'),('Alimi Sikiru', 'Forward'),('Franck Mawuena', 'Forward'),('Kayode Bankole', 'Goalkeeper')]
player = [('Nduka Junior', 2), ('Ahmed Akinyele',2), ('Jide Fatokun', 2), ('Ismaila Sodiq',2), ('Stanley Joseph', 2),('Olamilekan Adedayo',3),('Hadi Haruna',3),('Olamilekan Adams', 4),('Alimi Sikiru', 4),('Franck Mawuena', 4),('Kayode Bankole', 1)]
players = ['Nduka Junior','Ahmed Akinyele', 'Jide Fatokun','Ismaila Sodiq','Stanley Joseph','Olamilekan Adedayo','Hadi Haruna','Olamilekan Adams','Alimi Sikiru','Franck Mawuena',]
team = ['Enugu Rangers','Enyimba','Shooting Stars','Plateau Utd','Lobi Stars','Katsina Utd','Rivers Utd','Bendel','Sunshine Stars','Kano Pillars','Abia Warriors','Kwara United','Niger Tornadoes','Bayelsa United','Akwa United']
match = [('2024-01-01','Home', 1, 15), ('2024-02-01',  'Away', 1, 2),('2024-03-01', 'Home', 1, 3),('2024-04-01', 'Away', 1, 4),('2024-05-01',  'Home', 1, 1)]
matches = [1,2,3,4,5]
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

# Generate Player Metrics Data
competition_data = competition

# Generate Player Metrics Data
player_data = player

# Generate position Metrics Data
position_data = position

# Generate position Metrics Data
team_data = team

# Generate position Metrics Data
matches_data = match

# Generate Physical Metrics Data
physical_metrics_data = []
for _ in range(20):
    data = (
        random.choice(players),
        random.choice(matches),
        round(random.uniform(5000, 12000), 2),
        random.randint(10, 50),
        round(random.uniform(20, 35), 2),
        round(random.uniform(1, 5), 2),
        round(random.uniform(1, 5), 2)
    )
    physical_metrics_data.append(data)

# Generate Technical Metrics Data
technical_metrics_data = []
for _ in range(20):
    data = (
        random.choice(players),
        random.choice(matches),
        round(random.uniform(60, 100), 2),
        random.randint(0, 10),
        random.randint(0, 20),
        random.randint(0, 100)
    )
    technical_metrics_data.append(data)

# Generate Tactical Metrics Data
tactical_metrics_data = []
for _ in range(20):
    data = (
        random.choice(players),
        random.choice(matches),
        random.randint(0, 10),
        random.randint(0, 5),
        random.randint(0, 3),
        random.randint(0, 5),
        random.randint(0, 3)
    )
    tactical_metrics_data.append(data)

# Generate Physiological Metrics Data
physiological_metrics_data = []
for _ in range(20):
    data = (
        random.choice(players),
        random.choice(matches),
        round(random.uniform(60, 100), 2),
        round(random.uniform(90, 200), 2),
        round(random.uniform(60, 100), 2),
        round(random.uniform(20, 30), 2),
        round(random.uniform(30, 50), 2),
        round(random.uniform(0.8, 1.2), 2)
    )
    physiological_metrics_data.append(data)

# Generate Team Metrics Data
team_metrics_data = []
for _ in range(10):
    data = (
        random.choice(matches),
        random.randint(0, 5),
        random.randint(0, 5),
        round(random.uniform(0, 100), 2),
        round(random.uniform(0, 100), 2),
        random.randint(0, 20),
        random.randint(0, 20)
    )
    team_metrics_data.append(data)

# Generate Player Impact Metrics Data
player_impact_metrics_data = []
for _ in range(20):
    data = (
        random.choice(players),
        random.choice(matches),
        random.randint(0, 5),
        random.randint(0, 5),
        random.randint(0, 10),
        random.randint(0, 5),
        random.randint(0, 5)
    )
    player_impact_metrics_data.append(data)

# Generate Team Cohesion Metrics Data
team_cohesion_metrics_data = []
for _ in range(10):
    data = (
        random.choice(matches),
        round(random.uniform(50, 100), 2),
        round(random.uniform(50, 100), 2),
        round(random.uniform(50, 100), 2)
    )
    team_cohesion_metrics_data.append(data)

# Generate Psychological Metrics Data
psychological_metrics_data = []
for _ in range(20):
    data = (
        random.choice(players),
        random.choice(matches),
        round(random.uniform(50, 100), 2),
        round(random.uniform(50, 100), 2),
        round(random.uniform(50, 100), 2)
    )
    psychological_metrics_data.append(data)

# SQL Insert Statements
def generate_insert_statements(table_name, columns, data):
    insert_statements = []
    for row in data:
        if isinstance(row, tuple):
            values = ', '.join([f"'{str(v)}'" if isinstance(v, str) else str(v) for v in row])
        else:
            values = ', '.join([f"'{str(row)}'" if isinstance(row, str) else str(row)])
        statement = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({values});"
        insert_statements.append(statement)
    return insert_statements

# Define table columns
competition_columns = ['name']
position_columns = ['position']
player_columns = ['name','position_id']
team_columns = ['name']
match_columns = ['date','home_or_away','competition_id','opponent_id']
physical_columns = ['player', 'match', 'distance_covered', 'sprints', 'top_speed', 'acceleration', 'deceleration']
technical_columns = ['player', 'match', 'passing_accuracy', 'shots_on_target', 'dribbles_completed', 'touches']
tactical_columns = ['player', 'match', 'tackles', 'interceptions', 'clearances', 'blocks', 'fouls']
physiological_columns = ['player', 'match', 'heart_rate', 'blood_pressure', 'oxygen_saturation', 'body_temperature', 'recovery_time', 'fatigue_level']
teammetrics_columns = ['possession_percentage', 'goals_scored', 'expected_goals', 'goal_assist',  'shots_taken', 'shots_on_target', 'chances_created', 'conner_kicks_played', 'conner_kicks_converted', 'free_kicks_played', 'free_kicks_converted', 'goals_conceded', 'expected_goals_against', 'tackles_won', 'fouls_commited', 'yellow_card', 'red_card', 'interceptions', 'clearances', 'team', 'match']
player_impact_columns = ['player', 'match', 'goals', 'assists', 'key_passes', 'successful_dribbles', 'duels_won']
team_cohesion_columns = ['match', 'teamwork_score', 'communication_score', 'cohesion_score']
psychological_columns = ['player', 'match', 'motivation_level', 'stress_level', 'focus_level']

# Generate insert statements for all tables
competition_inserts = generate_insert_statements('metrics_competition', competition_columns, competition_data)
position_inserts = generate_insert_statements('metrics_position', position_columns, position_data)
player_inserts = generate_insert_statements('metrics_player', player_columns, player_data)
team_inserts = generate_insert_statements('metrics_team', team_columns, team_data)
match_inserts = generate_insert_statements('metrics_match', match_columns, matches_data)
physical_inserts = generate_insert_statements('PhysicalMetrics', physical_columns, physical_metrics_data)
technical_inserts = generate_insert_statements('TechnicalMetrics', technical_columns, technical_metrics_data)
tactical_inserts = generate_insert_statements('TacticalMetrics', tactical_columns, tactical_metrics_data)
physiological_inserts = generate_insert_statements('PhysiologicalMetrics', physiological_columns, physiological_metrics_data)
teammetrics_inserts = generate_insert_statements('TeamMetrics', teammetrics_columns, team_metrics_data)
player_impact_inserts = generate_insert_statements('PlayerImpactMetrics', player_impact_columns, player_impact_metrics_data)
team_cohesion_inserts = generate_insert_statements('TeamCohesionMetrics', team_cohesion_columns, team_cohesion_metrics_data)
psychological_inserts = generate_insert_statements('PsychologicalMetrics', psychological_columns, psychological_metrics_data)

# Print insert statements
print("\n".join(competition_inserts))
print("\n".join(position_inserts))
print("\n".join(player_inserts))
print("\n".join(team_inserts))
print("\n".join(match_inserts))
print("\n".join(physical_inserts))
print("\n".join(technical_inserts))
print("\n".join(tactical_inserts))
print("\n".join(physiological_inserts))
print("\n".join(teammetrics_inserts))
print("\n".join(player_impact_inserts))
print("\n".join(team_cohesion_inserts))
print("\n".join(psychological_inserts))