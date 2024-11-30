#reapating logic again and again
principal = 10000
rate = .06
term = 5
total interest = 0
  print ("principal")
  for x in range(5):
  interest = principal * rate
  print("interest" , interest)
  principal = principal + interest
  total interest = total interest + interest
  print ("toatl interest" , total interest)
  print("principal" , principal)
