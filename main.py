import copy
import random
from repository.Team import Team
from Participation import Participation


teamRepository = Team()
# participation = Participation()

teams = teamRepository.getAll()

leagueOneTeams = teams[:10]
# leagueTwoTeams = teams[10:]

leagueOneTeamsFix = copy.deepcopy(leagueOneTeams)
