#!/bin/bash
celery --app=tasks.tasks:celery worker -l INFO