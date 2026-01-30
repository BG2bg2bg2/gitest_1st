import importlib
import builtins
import pytest
import os
import importlib.util


def load_module():
    root = os.path.dirname(os.path.dirname(__file__))
    path = os.path.join(root, 'main.py')
    spec = importlib.util.spec_from_file_location('app_main', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_buy_item_success(monkeypatch):
    m = load_module()
    m.gold = 100
    items = m.get_shop_items()
    # pick a non-form affordable item (red shirt)
    idx = next(i for i, (name, info, cat) in enumerate(items, start=1) if name == 'red shirt')
    inputs = iter(['y', str(idx)])
    monkeypatch.setattr('builtins.input', lambda prompt='': next(inputs))
    m.shopping()
    assert 'red shirt' in m.invent
    assert m.gold == 80


def test_buy_item_insufficient(monkeypatch):
    m = load_module()
    m.gold = 5
    items = m.get_shop_items()
    idx = next(i for i, (name, info, cat) in enumerate(items, start=1) if name == 'red shirt')
    inputs = iter(['y', str(idx)])
    monkeypatch.setattr('builtins.input', lambda prompt='': next(inputs))
    m.shopping()
    assert 'red shirt' not in m.invent
    assert m.gold == 5


def test_closet_change_body(monkeypatch):
    m = load_module()
    # choose option 2 then 'wolf'
    inputs = iter(['2', 'wolf'])
    monkeypatch.setattr('builtins.input', lambda prompt='': next(inputs))
    m.closet()
    assert m.body_type == 'wolf'


def test_tutorial_selection(monkeypatch, capsys):
    m = load_module()
    # choose yes then first power
    inputs = iter(['y', '1'])
    monkeypatch.setattr('builtins.input', lambda prompt='': next(inputs))
    m.totor()
    captured = capsys.readouterr()
    assert 'Fly: Press F' in captured.out
