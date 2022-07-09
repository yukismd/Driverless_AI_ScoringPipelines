import java.io.IOException;
import ai.h2o.mojos.runtime.MojoPipeline;
import ai.h2o.mojos.runtime.frame.MojoFrame;
import ai.h2o.mojos.runtime.frame.MojoFrameBuilder;
import ai.h2o.mojos.runtime.frame.MojoRowBuilder;
import ai.h2o.mojos.runtime.lic.LicenseException;
import ai.h2o.mojos.runtime.utils.CsvWritingBatchHandler;
import com.opencsv.CSVWriter;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.io.Writer;

public class ExecuteDaiMojo {
 public static void main(String[] args) throws IOException, LicenseException {
    // Load model and csv
   String homePath = System.getProperty("user.home");
   final MojoPipeline model = MojoPipeline.loadFrom(homePath + "/Documents/Product/DAI/ScoringPipeline/MOJO_Java_Scoring_188/mojo-pipeline/pipeline.mojo");
   // Get and fill the input columns
    final MojoFrameBuilder frameBuilder = model.getInputFrameBuilder();
    final MojoRowBuilder rowBuilder = frameBuilder.getMojoRowBuilder();
   rowBuilder.setValue("x1", "2.60");
   rowBuilder.setValue("x2", "-3.21");
   rowBuilder.setValue("x3", "0.62");
   rowBuilder.setValue("x4", "1.36");
   frameBuilder.addRow(rowBuilder);
  // Create a frame which can be transformed by MOJO pipeline
  final MojoFrame iframe = frameBuilder.toMojoFrame();
  // Transform input frame by MOJO pipeline
  final MojoFrame oframe = model.transform(iframe);
  // `MojoFrame.debug()` can be used to view the contents of a Frame
  // oframe.debug();
  // Output prediction as CSV
  final Writer writer = new BufferedWriter(new OutputStreamWriter(System.out));
  final CSVWriter csvWriter = new CSVWriter(writer, '\n', '"', '"');
  CsvWritingBatchHandler.csvWriteFrame(csvWriter, oframe, true);
 }
}
