(defun facotorial (num)
	(setq total 1)
	(do ((i num (- i 1))) ((= i 1))
		(setq total (* total i))
	)
	total
)
(print "")
(print ( facotorial (read)))
