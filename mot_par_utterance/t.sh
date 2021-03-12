#!/bin/sh

. 00_init_paths.sh

# TODO : 
#	- AM : quinphones, MLP ....
#	- LM : perplexity on dev, native 4g, rnnLM


# triphones

steps/align_si.sh --boost-silence 1.25 --nj 100 --cmd "oar_queue.pl"  data/train lang_train exp/mono exp/mono_ali
steps/train_deltas.sh --boost-silence 1.25 --cmd "oar_queue.pl"  4200 40000 data/train lang_train exp/mono_ali exp/tri1
#utils/mkgraph.sh $WORK_DIR/lang/  $WORK_DIR/exp/tri1 $WORK_DIR/exp/tri1/graph
#steps/decode.sh --nj 6  $WORK_DIR/exp/tri1/graph  $WORK_DIR/data/dev $WORK_DIR/exp/tri1/decode_dev

# triphones + delta delta

steps/align_si.sh  --nj 100 --cmd "oar_queue.pl"  data/train lang_train exp/tri1 exp/tri1_ali
steps/train_deltas.sh --cmd "oar_queue.pl"  4200 40000 data/train lang_train exp/tri1_ali exp/tri2a
#utils/mkgraph.sh $WORK_DIR/lang/  $WORK_DIR/exp/tri2a $WORK_DIR/exp/tri2a/graph
#steps/decode.sh --nj 6  $WORK_DIR/exp/tri2a/graph  $WORK_DIR/data/dev $WORK_DIR/exp/tri2a/decode_dev

