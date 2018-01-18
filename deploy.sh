#!/usr/bin/env bash
mkdir .deploy || true
for f in .kube/*.yaml
do
 envsubst < $f > ".deploy/$(basename $f)"
done
