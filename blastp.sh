#!/bin/bash
blastp -query "$QUERY_FILE" -subject "$SUBJECT_FILE" -out "$OUT_FILE"
