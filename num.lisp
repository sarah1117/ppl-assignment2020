(defun nth-elt(elt list)
        "Return element number of ELT in list"
        (let((loc(length(member elt list))))
                (unless(zerop loc)
                        (-(length list)loc)
                )
        )
)       
