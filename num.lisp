(setq my_list '(01 10 20 30 40 50 60 70 80 90 ))

; my function
(defun nthele (n)
	(nth n my_list)
)

(print "List is:" )
(print my_list)
(print "Enter element number.")
(setq n ( read )) 
; to print the output.
(print ( nthele n))
(print "")
