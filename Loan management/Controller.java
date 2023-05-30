import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/loans")
public class LoanController {

    private final LoanRepository loanRepository;

    @Autowired
    public LoanController(LoanRepository loanRepository) {
        this.loanRepository = loanRepository;
    }

    @PostMapping
    public ResponseEntity<Loan> createOrUpdateLoan(@RequestBody Loan loan) {
        if (loan.getId() != null) {
            if (loanRepository.existsById(loan.getId())) {
                Loan updatedLoan = loanRepository.save(loan);
                return ResponseEntity.ok(updatedLoan); // Return the updated Loan object
            } else {
                return ResponseEntity.status(HttpStatus.NOT_FOUND).body(null);
            }
        } else {
            Loan createdLoan = loanRepository.save(loan);
            return ResponseEntity.ok(createdLoan); // Return the created Loan object
        }
    }
}
