import pytest
import project

def test_restart_game():
    #setting arbitrary initial values
    project.falling_objects = ['apple', 'bomb']
    project.score = 10
    project.hearts = 2
    project.game_over = True
    project.magnet_active = True
    project.magnet_timer = 100
    project.bomb_speed_multiplier = 2

    project.restart_game()

    #testing
    assert project.falling_objects == []
    assert project.score == 0  
    assert project.hearts == 5  
    assert not project.game_over 
    assert not project.magnet_active  
    assert project.magnet_timer == 0  
    assert project.bomb_speed_multiplier == 1  

def test_display_hearts():
    try:
        project.display_hearts()
    except: #fail explicitly if the function throws an error
        pytest.fail('Hearts could not be displayed properly')

def test_game_over_screen():
    try:
        project.game_over_screen()
    except: #fail explicitly if the function throws an error
        pytest.fail('Game Over screen could not be displayed properly')

def test_pause_screen():
    try:
        project.pause_screen()
    except: #fail explicitly if the function throws an error
        pytest.fail('Pause screen could not be displayed properly')