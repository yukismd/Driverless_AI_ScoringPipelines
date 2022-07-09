import java.io.IOException;
import java.io.File;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.io.Writer;
import com.opencsv.CSVWriter;

import ai.h2o.mojos.runtime.MojoPipeline;
import ai.h2o.mojos.runtime.api.MojoPipelineService;
import ai.h2o.mojos.runtime.frame.MojoFrame;
import ai.h2o.mojos.runtime.frame.MojoFrameBuilder;
import ai.h2o.mojos.runtime.frame.MojoRowBuilder;
import ai.h2o.mojos.runtime.lic.LicenseException;
import ai.h2o.mojos.runtime.utils.CsvWritingBatchHandler;


public class ExecuteDaiMojo {
    public static void main(String[] args) throws IOException, LicenseException {
        // Load model and csv
        final MojoPipeline model = MojoPipelineService.loadPipeline(new File("/Users/YShimada-MBP16/Documents/Learning/Java/dai_mojo/mojo-pipeline/pipeline.mojo"));

        // Get and fill the input columns
        final MojoFrameBuilder frameBuilder = model.getInputFrameBuilder();
        final MojoRowBuilder rowBuilder = frameBuilder.getMojoRowBuilder();
        rowBuilder.setValue("CRIM", "0.00632");
        rowBuilder.setValue("ZN", "18");
        rowBuilder.setValue("INDUS", "2.31");
        rowBuilder.setValue("CHAS", "0");
        rowBuilder.setValue("NOX", "0.538");
        rowBuilder.setValue("RM", "6.575");
        rowBuilder.setValue("AGE", "65.2");
        rowBuilder.setValue("DIS", "4.09");
        rowBuilder.setValue("RAD", "1");
        rowBuilder.setValue("TAX", "296");
        rowBuilder.setValue("PTRATIO", "15.3");
        rowBuilder.setValue("B", "396.9");
        rowBuilder.setValue("LSTAT", "4.98");
        frameBuilder.addRow(rowBuilder);

        // Create a frame which can be transformed by MOJO pipeline
        final MojoFrame iframe = frameBuilder.toMojoFrame();

        // Transform input frame by MOJO pipeline
        final MojoFrame oframe = model.transform(iframe);
        // `MojoFrame.debug()` can be used to view the contents of a Frame
        // oframe.debug();

        // Output prediction as CSV
        final Writer writer = new BufferedWriter(new OutputStreamWriter(System.out));
        final CSVWriter csvWriter = new CSVWriter(writer);
        CsvWritingBatchHandler.csvWriteFrame(csvWriter, oframe, true);
    }
}