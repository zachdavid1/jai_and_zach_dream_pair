import pytest
from scripts import Person, Tracker
def test_scipt():
    p1 = Person("Jai", [27, 8, 2005])
    p2 = Person("Zach", [2, 10, 2008])

    tracker = Tracker([1,10,2026])
    tracker.add_friend(p1)
    tracker.add_friend(p2)
    assert tracker.friends == [p1, p2]
    tracker.edit_name('Jai', 'Jaishimmy')
    assert p1.name == 'Jaishimmy'
    assert p1.bday == [27,8,2005]
    assert tracker.upcoming_bdays() == {"Zach": 18}
    
    
    tracker.edit_bday([27,8,2005], [15,1,2005])
    tracker.today = [10,12,2026]
    assert tracker.upcoming_bdays() == {"Jaishimmy": 22}


