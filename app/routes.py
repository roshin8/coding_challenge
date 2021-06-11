import logging

import flask
from flask import Flask, Response, request, jsonify
from app.stats import get_github_stats, get_bitbucket_stats

app = Flask("user_profiles_api")
logger = flask.logging.create_logger(app)
logger.setLevel(logging.INFO)


@app.route("/health-check", methods=["GET"])
def health_check():
    """
    Endpoint to health check API
    """
    app.logger.info("Health Check!")
    return Response("All Good!", status=200)


@app.route("/org-stats-agg", methods=["GET"])
def org_stats_aggregator():
    """
    Endpoint to aggregate stats from repos from Bitbucket and GitHub
    """
    app.logger.info("Organisation Stats Aggregator!")
    try:
        github_stats = get_github_stats(request.args.get('github_org'))
        bitbucket_stats = get_bitbucket_stats(request.args.get('bitbucket_team'))
    except ConnectionError as e:
        return Response(str(e), status=500)

    return jsonify(github_stats.serialize(), bitbucket_stats.serialize())
