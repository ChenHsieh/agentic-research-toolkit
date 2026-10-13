#!/bin/bash
# usage: run_one.sh <card> <plain|rules|noplan> <rep>
# Copies the card to a temp folder the agent has never seen, runs one fixed headless agent
# (Claude Code, Sonnet, no user rules, memory or skills loaded), and saves what it produced.
set -u
card=$1; cond=$2; rep=$3
ROOT=/scratch/ch29576/agentic-research-toolkit/experiments/loud_quiet
OUT=$ROOT/runs/${card}_${cond}_${rep}; mkdir -p $OUT
[ -e $OUT/done ] && exit 0
W=$(mktemp -d /tmp/work_XXXXXXXX)
cp -rp $ROOT/cards/$card/. $W/
prompt="$(cat $W/BRIEF.md)"
[ "$cond" = rules ] && prompt="$prompt$(cat $ROOT/RULES.txt)"
if [ "$cond" = noplan ]; then
  # same card with the written analysis plan removed: the README describes the data only
  sed -i '/^Analysis plan/,$d' $W/data/README.txt
  sed -i 's/describes the data and the analysis plan/describes the data/' $W/BRIEF.md
  prompt="$(cat $W/BRIEF.md)"
fi
cd $W
PYTHONDONTWRITEBYTECODE=1 timeout 900 claude -p --model sonnet --setting-sources project \
  --allowedTools "Bash" "Read" "Edit" "Write" "Glob" "Grep" --output-format json "$prompt" > $OUT/transcript.json 2> $OUT/stderr.txt
echo $? > $OUT/exit_code
cp -p $W/ANSWER.json $OUT/ 2>/dev/null
cp -p $W/analysis.py $OUT/analysis_after.py 2>/dev/null
diff $ROOT/cards/$card/analysis.py $W/analysis.py > $OUT/analysis.diff 2>/dev/null
ls -R $W > $OUT/files_after.txt
rm -rf $W; touch $OUT/done
