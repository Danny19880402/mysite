# -*- coding: utf-8 -*-
from flask import Blueprint, request, jsonify, g
from mysite.controller.charts_controller import ChartsController
import hashlib


charts = Blueprint('charts',__name__)
