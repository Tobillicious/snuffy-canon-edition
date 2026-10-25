namespace Snuffy.DecoderRetraction

structure DecoderPair (A B : Type*) where
  encode : A → B
  decode : B → A
  retraction : ∀ a, decode (encode a) = a

theorem decode_encode {A B : Type*} (D : DecoderPair A B) (a : A) :
    D.decode (D.encode a) = a :=
  D.retraction a

end Snuffy.DecoderRetraction