(defun facotorial2 (num &optional (temp num))
	(if (= num 1)
		temp
	( facotorial2 (- num 1) (* (- num 1) temp ))
	)
)
(print ( facotorial2 (read)))
(print "")
